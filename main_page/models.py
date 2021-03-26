from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id    = models.IntegerField(primary_key=True)
    location    = models.CharField(max_length=100)
    num_rooms   = models.IntegerField()
    occupancy   = models.IntegerField()
    rating      = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return f"{{hotel_id: {self.hotel_id}, location: {self.location}, num_rooms: {self.num_rooms}, occupancy: {self.occupancy}, rating: {self.rating}}}"


class Reservation(models.Model):
    reservation_id      = models.IntegerField(primary_key=True)
    check_in_date       = models.DateField()
    check_out_date      = models.DateField()
    guest_id            = models.IntegerField()
    payment_type        = models.CharField(max_length=10)
    credit_card_number  = models.CharField(max_length=20)
    total               = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{{reservation_id: {self.reservation_id}, check_in_date: {self.check_in_date}, check_out_date: {self.check_out_date}, guest_id: {self.guest_id}, payment_type: {self.payment_type}, credit_card_number: {self.credit_card_number}, total: {self.total}}}"