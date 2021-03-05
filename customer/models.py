from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=25)
    emailID = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    date_of_birth = models.DateTimeField('date published')
    # address = models.TextField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
