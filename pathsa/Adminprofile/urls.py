from django.urls import path
from . import views
app_name='profile'
urlpatterns=[
    path('',views.Adminprofile),
    path('editprofile/',views.Editprofile,name='editprofile')
    
    
]