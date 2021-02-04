from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=25)
    emailID = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    date_of_birth = models.DateTimeField('date published')
    address = models.TextField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)

class Hotel(models.Model):
    hotel_id = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=30)
    hotel_address = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    email_id = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()

class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    total_rooms = models.IntegerField()
    room_no = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=20)
    capacity_of_person = models.IntegerField(default=1)
    image = models.ImageField()
    price = models.IntegerField(default=0)

class Booking(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    booking_id = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    persons = models.IntegerField()

class Payment(models.Model):
    booking_id = models.ForeignKey(Booking,on_delete=models.CASCADE)
    amount = models.IntegerField()
