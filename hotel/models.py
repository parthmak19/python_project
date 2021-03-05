from django.db import models


# Create your models here.

class Hotel(models.Model):
    hotel_id = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=30)
    hotel_address = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    email_id = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()

class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    total_rooms = models.IntegerField()
    room_no = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=20)
    capacity_of_person = models.IntegerField(default=1)
    image = models.ImageField()
    price = models.IntegerField(default=0)
