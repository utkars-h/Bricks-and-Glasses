from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Owner(models.Model):
    ownerID = models.IntegerField()
    oname = models.CharField(max_length=40)
    contact = PhoneNumberField()
    email = models.EmailField()
    pwd = models.CharField(max_length=40)
