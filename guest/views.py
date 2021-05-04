from django.shortcuts import render, redirect
from django.db import connection, transaction
from guest.models import Guest, Reservation, ReservationRoomRel, Room, Hotel, Feature, FeatureRoomRel
from .forms import ReservationForm, CreateUserForm, FilterForm
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def registerUser(request):
    form = CreateUserForm(request.POST)
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()

            # save user in guest database
            guest_ids = [guest.guest_id for guest in Guest.objects.all()]
            available_ids = [g_id for g_id in range(1, max(guest_ids)+2) if g_id not in guest_ids]
            next_guest_pk = available_ids[0]
            g = Guest()
            g.guest_id = next_guest_pk
            g.username = form.cleaned_data.get('username')
            g.first = form.cleaned_data.get('firstname')
            g.last = form.cleaned_data.get('lastname')
            g.save()            

            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('login')

    context = {'form': form}

    return render(request, 'guest/register.html', context)

def loginUser(request):

    if(request.method =='POST'):            # if form has been submitted
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            g_id = Guest.objects.all().filter(username=username)[0].guest_id
            print('valid user ' + str(g_id) + username)
            login(request, user)

            # TODO :find id against username, from local db and add here
            return redirect('guest_home')

    context = {}
    return render(request, 'guest/login.html', context)

def logoutUser(request):
    logout(request)
    context = {}
    return redirect('login')


def updateRoomAvailability(request, room_id):
     # STORED PROCEDURE
    with connection.cursor() as cursor:
        cursor.callproc("updtRoomAvailable", [room_id,] )
        # cursor.execute('CREATE PROCEDURE UpdateRoomTable AS UPDATE room SET available = 0 where room_id = room_id') 
        cursor.close()
                    

def filterByPrice(request):
    username = request.user
    guest_id = Guest.objects.get(username=username).guest_id
    guest = Guest.objects.get(guest_id=guest_id)
    hotels = []

    print('guest_id = ', guest_id)
    print('username = ', username)

    form = FilterForm(request.POST)
    if(request.method == 'POST'):

        form = FilterForm(request.POST)
        
        if(form.is_valid()):
            lower_p = form.cleaned_data.get('lower_price')

            lp = int(request.POST['lower_price'])

            #'select h.hotel_id, location, room_type, price_per_night, check_in_time, check_out_time from hotel h inner join room r on r.hotel_id = h.hotel_id where price_per_night > %d;
            with connection.cursor() as cursor:
                cursor.execute( 'select h.hotel_id, location from hotel h inner join room r on r.hotel_id = h.hotel_id where price_per_night > %d;' % lp)
                columns = [col[0] for col in cursor.description]
                ans = cursor.fetchall()

                # STILL TO DO 
                # add pair here, 

            context = {'hotels': hotels}
            return render(request, 'guest/make_reservation.html', context = {'hotels': hotels})
            # return HttpResponseRedirect(reverse('make_a_reservation', kwargs={context}))

    context = {'form': form}
    return render(request, 'guest/findOpenReservations.html', context)

def home(request):
    username = request.user
    guest_id = Guest.objects.get(username=username).guest_id
    # print(request.user.is_authenticated)
    guest = Guest.objects.get(guest_id=guest_id)
    reservations = Reservation.objects.all().filter(guest_id=guest_id)

    selected_reservation_id = None
    selected_res_info = None
    num_selected_rooms = None
    if "get_reservation" in request.GET:    # User has selected one of their reservations, get info for that reservation
        selected_reservation_id = int(request.GET.get('get_reservation'))
        print(f"\nTrying to get info for reservation {selected_reservation_id}\n")

        selected_res_room_rel = ReservationRoomRel.objects.all().filter(reservation_id=selected_reservation_id)
        selected_rooms = [rel.room for rel in selected_res_room_rel]
        num_selected_rooms = len(selected_rooms)

        room_feature_set = []
        for room in selected_rooms:
            room_feature_rel = FeatureRoomRel.objects.all().filter(room_id=room.room_id)
            features = [rel.feature for rel in room_feature_rel]
            room_feature_set.append(features)
        
        selected_res_info = zip(selected_rooms, room_feature_set)

    elif "delete_reservation" in request.GET:
        del_res_id = int(request.GET.get('delete_reservation'))
        print(f"\nTrying to delete reservation {del_res_id}\n")
        with connection.cursor() as cursor:
            cursor.callproc('DeleteReservation', [del_res_id])  # Calling the DeleteReservation stored procedure

    
    hotels = []
    for reservation in reservations:
        res_room_rel = ReservationRoomRel.objects.all().filter(reservation_id=reservation.reservation_id)
        sample_room = res_room_rel[0].room

        hotel = Hotel.objects.get(hotel_id=sample_room.hotel_id)
        hotels.append(hotel)
    
    # Zipping hotel and reservation lists so that we can loop through the pairs in home.html
    reservations_and_hotels = zip(reservations, hotels)

    context = {
        # 'guest_id': guest_id,
        'guest_name': f"{guest.first} {guest.last}",
        'reservations_and_hotels': reservations_and_hotels,
        'selected_reservation_id': selected_reservation_id,
        'selected_res_info': selected_res_info,
        'num_selected_rooms': num_selected_rooms,
        # The following two lines aren't used right now since we have the zipped list, but sending anyway
        'reservations': reservations,
        'hotels': hotels
    }

    return render(request, 'guest/home.html', context)


def make_reservation(request):

    print('incoming request = ')
    print(request)

    username = request.user
    guest_id = Guest.objects.get(username=username).guest_id
    guest = Guest.objects.get(guest_id=guest_id)

    hotels = Hotel.objects.all()

    print("gyest values  ", guest)          # debugging
    print("hotel value  ", hotels)          # debugging

    selected_hotel_id = None
    selected_room_bundle = [('asdf', 'If you are reading this than something has gone wrong')]
    if "select_hotel" in request.GET:   # User has selected a hotel, get room data for that hotel to pass to form

        selected_hotel_id = int(request.GET.get('select_hotel'))
        selected_rooms = Room.objects.all().filter(hotel_id=selected_hotel_id)
        selected_room_bundle = []
        for room in selected_rooms:     # For each room, make a description that will be included in the form
            room_feature_rel = FeatureRoomRel.objects.all().filter(room_id=room.room_id)
            feature_names = [rel.feature.feature for rel in room_feature_rel]
            room_desc_str = f"{room.room_type}: "
            if len(feature_names) > 0:
                room_desc_str += ', '.join(feature_names) + ", "
            room_desc_str += f"${room.price_per_night} per night"
            selected_room_bundle.append((room.room_id, room_desc_str))

    print("selected room bundle: ", selected_room_bundle)

    reservation_form = ReservationForm(selected_room_bundle)
    if request.POST:
        reservation_form = ReservationForm(selected_room_bundle, request.POST)
    success = -1    # Variable used to determine what message should be shown
    if request.POST:
        if reservation_form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute('SET TRANSACTION ISOLATION LEVEL REPEATABLE READ')

            next_res_pk = None

            try:
                with transaction.atomic():
                    cd = reservation_form.cleaned_data
                    print(f"\033[92m{cd}\033[0m")
                    room_id = cd['room']
                    room = Room.objects.get(room_id=room_id)

                    # CHECK IF ROOM AVAILABLE - SANITY
                    if (room.available == 1):
                        
                        delta = cd['check_out_date'] - cd['check_in_date']
                        duration = delta.days

                        room_feature_rel = FeatureRoomRel.objects.all().filter(room_id=room_id)
                        feature_total = sum([rel.feature.price for rel in room_feature_rel])
                        total = (room.price_per_night + feature_total) * duration

                        reservation_ids = [res.reservation_id for res in Reservation.objects.all()]
                        # available_ids = [res_id for res_id in range(1, max(reservation_ids)+2) if res_id not in reservation_ids]
                        available_ids = [1] if (reservation_ids==None or len(reservation_ids) == 0) else [res_id for res_id in range(1, max(reservation_ids)+2) if res_id not in reservation_ids]
                        next_res_pk = available_ids[0]


                        # Make credit card number compulsory for credit card option

                        new_reservation = Reservation(
                            reservation_id = next_res_pk,
                            guest_id=guest_id,
                            check_in_date=cd['check_in_date'],
                            check_out_date=cd['check_out_date'],
                            payment_type=cd['payment_type'],
                            credit_card_number=cd['credit_card_number'] if len(cd['credit_card_number'])>0 else None,
                            total=total
                        )
                        new_reservation.save()

                        # DELIMITER //
                        # CREATE PROCEDURE unReserveRoom (
                        #     r_id INT
                        # )
                        # BEGIN
                        #     UPDATE room 
                        #         SET available=0
                        #         WHERE room_id = r_id;
                        # END //
                        # DELIMITER ;

                        # Changing Room Availability ONCE RESERVED 
                        # room = Room.objects.get(room_id=room_id)
                        # room.available= 0
                        # print('room reserved, not available anymore ')
                        # room.save()

                        print('executing cursor to make room unavailable' + str(room_id))
                        with connection.cursor() as cursor:
                            cursor.callproc('unReserveRoom', [room_id])

                        res_room_rel_ids = [res.id for res in ReservationRoomRel.objects.all()]
                        available_ids = [1] if (res_room_rel_ids==None or len(res_room_rel_ids) == 0) else [rel_id for rel_id in range(1, max(res_room_rel_ids)+2) if rel_id not in res_room_rel_ids]
                        # available_ids = [rel_id for rel_id in range(1, max(res_room_rel_ids)+2) if rel_id not in res_room_rel_ids]
                        next_res_room_rel_pk = available_ids[0]

                        new_res_room_rel = ReservationRoomRel(id=next_res_room_rel_pk, reservation=new_reservation, room=room)
                        new_res_room_rel.save()

            except IntegrityError:
                print("There was an integrity error")
            
            if next_res_pk:
                verify_res = Reservation.objects.all().filter(reservation_id=next_res_pk)
                verify_rel = ReservationRoomRel.objects.all().filter(reservation=next_res_pk)
                success = 1 if (len(verify_res) > 0 and len(verify_rel) > 0) else 0
            else:
                success = 0


        else:
            print(f"\033[93mReservation form invalid.\n{reservation_form.errors}\033[0m")
    reservation_form = ReservationForm(selected_room_bundle)

    print(f"Suceess : {success}")

    context = {
        'guest_id': guest_id,
        'guest_name': f"{guest.first} {guest.last}",
        'hotels': hotels,
        'selected_hotel_id': selected_hotel_id,
        'reservation_form': reservation_form,
        'success': success
    }

    return render(request, 'guest/make_reservation.html', context)

