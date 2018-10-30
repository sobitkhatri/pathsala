from django import forms
from .models import image
from django.contrib.auth.models import User
from homepage.models import Profile
from django.contrib.auth.forms import UserChangeForm

class profilepicupdate(forms.ModelForm):
    class Meta:
        model=image  
        fields=['profile_image']  



class adminform(UserChangeForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']   

#class adminform2(forms.ModelForm):
 #   class Meta:
  #      model=Profile
   #     fields=['Adminstrative_name','DateOfEstablish','Adress','City','Country','Contact_no','Adminstrative_type']
