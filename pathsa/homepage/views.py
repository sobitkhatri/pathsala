from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import adminform,adminform2
from django.contrib.auth.models import User
from pathsa import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



def adminformview(request):
    if request.method=='POST':
        form1=adminform(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            email=form1.cleaned_data['email']
            first_name=form1.cleaned_data['first_name']
            last_name=form1.cleaned_data['last_name']
            password=form1.cleaned_data['password']
            form1.save()
            return redirect('homepage:logincomform')
    else:
        form1=adminform()
    settings.LOGIN_REDIRECT_URL='/admin'    
    return render(request,'homepage/adminform.html',{'form1':form1})

    
@login_required(login_url="homepage:logincomform")
def adminformview2(request):
    if request.method=="POST":
        form2=adminform2(request.POST)
        if form2.is_valid():
            Adminstrative_name=form2.cleaned_data['Adminstrative_name']
            DateOfEstablish=form2.cleaned_data['DateOfEstablish']
            City=form2.cleaned_data['City']
            Country=form2.cleaned_data['Country']
            Principal_Phone_No=form2.cleaned_data['Principal_Phone_No']
            Contact_no=form2.cleaned_data['Contact_no']
            Adminstrative_type=form2.cleaned_data['Adminstrative_type']

            instance=form2.save(commit=False)
            instance.Author=request.user
            instance.save()
            return redirect('/adminprofile')

    else:
        form2=adminform2()
    return render(request,'homepage/adminform2.html',{'form2':form2})


def logincomform(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect("/adminprofile")
            else:        
                return redirect('homepage:adminform2')
    else:
        form=AuthenticationForm()
    return render(request,'homepage/logincomform.html',{'form':form})    




def editprofile2(request):
    if request.method=='POST':
        form=adminform2(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/adminprofile')
    else:
        form=adminform2(instance=request.user.profile)
    return render(request,'homepage/editprofile2.html',{'form':form})        