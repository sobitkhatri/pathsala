from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


class Profile(models.Model):
    Author = models.OneToOneField(User, unique=True, related_name='profile',on_delete=models.CASCADE)
    Adminstrative_name=models.CharField(max_length=200)
    DateOfEstablish=models.CharField(max_length=100)
    Adress=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Country=CountryField()
    Principal_Phone_NO=PhoneNumberField()
    Contact_no=PhoneNumberField()
    Adminstrative_type=models.CharField(max_length=100)
 
    
    
    def formatted_phone(self, country=None):
        return phonenumbers.parse(self.Principal_Phone_NO, country)



    def __str__(self):
        profile='profile:'+self.Adminstrative_name
        return profile


    







