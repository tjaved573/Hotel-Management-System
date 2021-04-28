from django.db import models


class Guest(models.Model):
    class Meta:
        db_table = 'guest'
    
    guest_id    = models.IntegerField(primary_key=True)
    username    = models.CharField(max_length=50)
    first       = models.CharField(max_length=20)
    last        = models.CharField(max_length=20)

    def __str__(self):
        return f"{{{self.first} {self.last}, username: {self.username}, guest_id: {self.guest_id}}}"


class Reservation(models.Model):
    class Meta:
        db_table = 'reservation'

    reservation_id      = models.IntegerField(primary_key=True)
    check_in_date       = models.DateField()
    check_out_date      = models.DateField()
    guest_id            = models.IntegerField()
    payment_type        = models.CharField(max_length=10)
    credit_card_number  = models.CharField(max_length=20)
    total               = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{{reservation_id: {self.reservation_id}, check_in_date: {self.check_in_date}, check_out_date: {self.check_out_date}, guest_id: {self.guest_id}, payment_type: {self.payment_type}, credit_card_number: {self.credit_card_number}, total: {self.total}}}"
    

class ReservationRoomRel(models.Model):
    # We need this model in guest to (at least) access the hotel name through reservation->room->hotel.location
    class Meta:
        unique_together = [['reservation_id', 'room_id']]
    
    reservation  = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    room         = models.ForeignKey('Room', on_delete=models.CASCADE)



class Room(models.Model):
    class Meta:
        db_table = 'room'
    
    room_id         = models.IntegerField(primary_key=True)
    hotel_id        = models.IntegerField()
    room_type       = models.CharField(max_length=20)
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    available       = models.IntegerField()
    check_in_time   = models.TimeField()
    check_out_time  = models.TimeField()


class Hotel(models.Model):
    class Meta:
        db_table = 'hotel'
    
    hotel_id    = models.IntegerField(primary_key=True)
    location    = models.CharField(max_length=20)
    num_rooms   = models.IntegerField()
    occupancy   = models.IntegerField()
    rating      = models.DecimalField(max_digits=4, decimal_places=3)
    

