from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from homepage.models import Profile
from .forms import profilepicupdate
from .forms import adminform



def Editprofile(request):
    if request.method=='POST':
        profile_pic=profilepicupdate(request.POST,request.FILES,instance=request.user.image)
        profileform1=adminform(request.POST,instance=request.user)


        if profile_pic.is_valid()  and profileform1.is_valid():
            profile_pic.save()
            profileform1.save()
            return redirect('/adminprofile')

    else:        
        profile_pic=profilepicupdate(request.FILES,instance=request.user.image)
        profileform1=adminform(instance=request.user)
        

    update={
        'profile_pic':profile_pic,
        'profileform1':profileform1,

    } 

    return render(request,'adminprofile/editprofile.html',update)



@login_required(login_url="homepage:logincomform")
def Adminprofile(request):
    return render(request,'adminprofile/profile.html')




