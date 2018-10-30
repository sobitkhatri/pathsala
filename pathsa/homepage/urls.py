from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name='homepage'


urlpatterns=[
    path('adminform1',views.adminformview, name='adminform1'),
    path('adminform2',views.adminformview2, name='adminform2'),
    path('logincomform/',views.logincomform,name='logincomform'),
    path('editprofile/',views.editprofile2,name='editprofile')

]