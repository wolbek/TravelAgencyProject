from django.shortcuts import render,redirect,get_object_or_404
from .models import Flight
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'flight/home.html')

def about(request):
    return render(request,'flight/about.html')

@login_required
def flight(request):
    return render(request,'flight/flight.html')

@login_required
def availableflight(request):
    if request.GET.get('returndate'):
        flights=Flight.objects.filter(available=True,location1=request.GET['location1'],location2=request.GET['location2'],departuredate=request.GET['departuredate'],returndate=request.GET['returndate'])

    else:
        flights=Flight.objects.filter(available=True,location1=request.GET['location1'],location2=request.GET['location2'],departuredate=request.GET['departuredate'])
    return render(request,'flight/availableflight.html',{'flights':flights})

@login_required
def payment(request,flight_id):
    flight=get_object_or_404(Flight,pk=flight_id)
    return render(request,'flight/payment.html',{'flight':flight})

def signupuser(request):
    if request.method=="GET":
        return render(request,'flight/signupuser.html')
    else:        
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'flight/signupuser.html',{'error':"That username has already been taken"})
        else:
            return render(request,'flight/signupuser.html',{'error':"Password did not match"})
      

def loginuser(request):
    if request.method=="GET":
        return render(request,'flight/loginuser.html')
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'flight/loginuser.html',{'error':"Username and password did not match"})
        else:
            login(request,user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')
