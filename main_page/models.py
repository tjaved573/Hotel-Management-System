from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id    = models.IntegerField(primary_key=True)
    location    = models.CharField(max_length=100)
    num_rooms   = models.IntegerField()
    occupancy   = models.IntegerField()
    rating      = models.DecimalField(max_digits=4, decimal_places=3)