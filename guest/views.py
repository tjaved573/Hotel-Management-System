from django.shortcuts import render
from guest.models import Guest, Reservation, ReservationRoomRel, Room, Hotel


def home(request, guest_id):
    guest = Guest.objects.get(guest_id=guest_id)
    guest_reservations = Reservation.objects.all().filter(guest_id=guest_id)
    print(guest_reservations)

    # Getting hotels associated with each reservation
    hotels = []
    for reservation in guest_reservations:
        res_room_rel = ReservationRoomRel.objects.get(reservation_id=reservation.reservation_id)
        room = res_room_rel.room
        hotel = Hotel.objects.get(hotel_id=room.hotel_id)
        hotels.append(hotel)
    
    # Zipping hotel and reservation lists so that we can loop through the pairs in home.html, no other way to do this
    paired_hotels_and_reservations = zip(hotels, guest_reservations)

    context = {
        'guest_id': guest_id,
        'guest_name': f"{guest.first} {guest.last}",
        'paired_hotels_and_reservations': paired_hotels_and_reservations,
        # The following two lines aren't used right now since we have the zipped list, but sending anyway
        'reservations': guest_reservations,
        'hotels': hotels
    }

    return render(request, 'guest/home.html', context)
