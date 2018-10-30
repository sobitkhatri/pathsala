from django.db import models
from django.db import models
from django.contrib.auth.models import User



class image(models.Model):
    auther=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.auther.username}:profile_image'

  
