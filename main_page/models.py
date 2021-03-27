from django.db import models

# Create your models here.
class Hotel(models.Model):
    class Meta:
        db_table = 'hotel'

    hotel_id    = models.IntegerField(primary_key=True)
    location    = models.CharField(max_length=100)
    num_rooms   = models.IntegerField()
    occupancy   = models.IntegerField()
    rating      = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return f"{{hotel_id: {self.hotel_id}, location: {self.location}, num_rooms: {self.num_rooms}, occupancy: {self.occupancy}, rating: {self.rating}}}"


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


class Feature(models.Model):
    class Meta:
        db_table = 'features'
    
    feature_id      = models.IntegerField(primary_key=True)
    feature         = models.CharField(max_length=20)
    price           = models.DecimalField(max_digits=9, decimal_places=2)
    description     = models.CharField(max_length=255)

    def __str__(self):
        return f"{{feature_id: {self.feature_id}, feature: {self.feature}, price: {self.price}, description: {self.description}}}"

# class Guest(models.Model):
#     guest_id = models.IntegerField(primary_key=True)
#     first = models.CharField(max_length=20)
#     last = models.CharField(max_length=20)



# class Room(models.Model):
#     room_id = models.IntegerField(primary_key=True)
#     hotel_id = models.IntegerField()
#     room_type = models.CharField(max_length=20)
#     price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
#     available = models.IntegerField()
#     check_in_time = models.TimeField()
#     check_out_time = models.TimeField()




