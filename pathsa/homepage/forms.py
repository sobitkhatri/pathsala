from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django_countries.fields import CountryField
import phonenumbers
from phonenumber_field.formfields import PhoneNumberField




class adminform(UserCreationForm):
    email=forms.EmailField()
    class Meta():
        model=User
        fields=['username','email','first_name','last_name','password']




class adminform2(forms.ModelForm):
    Adminstrative_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Adminstrative_Name'}),required=True,max_length=200)
    DateOfEstablish=forms.CharField(max_length=100)
    Adress=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'principal_name'}),required=True,max_length=100) 
    City=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),required=True,max_length=100)
    Country=CountryField()
    Principal_Phone_No=PhoneNumberField()
    Contact_no=PhoneNumberField()
    Adminstrative_type=forms.CharField(max_length=100)

    class Meta():
        model=Profile
        fields=['Adminstrative_name','DateOfEstablish','Adress','City','Country','Principal_Phone_No','Contact_no','Adminstrative_type']


    
        
      
   
