from django.shortcuts import render
from guest.models import Guest, Reservation, ReservationRoomRel, Room, Hotel, Feature, FeatureRoomRel
from .forms import ReservationForm


def home(request, guest_id):
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
    
    hotels = []
    for reservation in reservations:
        res_room_rel = ReservationRoomRel.objects.all().filter(reservation_id=reservation.reservation_id)
        sample_room = res_room_rel[0].room

        hotel = Hotel.objects.get(hotel_id=sample_room.hotel_id)
        hotels.append(hotel)
    
    # Zipping hotel and reservation lists so that we can loop through the pairs in home.html
    reservations_and_hotels = zip(reservations, hotels)

    context = {
        'guest_id': guest_id,
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


def make_reservation(request, guest_id):
    guest = Guest.objects.get(guest_id=guest_id)
    hotels = Hotel.objects.all()

    selected_hotel_id = None
    selected_room_bundle = [(None, 'If you are reading this than something has gone wrong')]
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

    reservation_form = ReservationForm(selected_room_bundle)    # Bundled array of (room_id, description) values -> make form

    context = {
        'guest_id': guest_id,
        'guest_name': f"{guest.first} {guest.last}",
        'hotels': hotels,
        'selected_hotel_id': selected_hotel_id,
        'reservation_form': reservation_form,
    }

    return render(request, 'guest/make_reservation.html', context)

