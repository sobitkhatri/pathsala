from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(template_name='homepage/homepage.html'),name='home'),
    path('adminform/',include('homepage.urls'),name='adminform'),
    path('adminprofile/',include('Adminprofile.urls'),name='Adminprofile'),
   

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


