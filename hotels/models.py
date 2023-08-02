from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_id = models.TextField()
    url = models.TextField()
    text = models.TextField()
    title_url_hotel = models.TextField()
    hotel_name = models.TextField()
    hotel_address = models.TextField()
    number_of_room = models.TextField()