from django.shortcuts import render,redirect,get_object_or_404
from .models import Train
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.

@login_required
def train(request):
    return render(request,'train/train.html')

@login_required
def availabletrain(request):
    trains=Train.objects.filter(available=True,location1=request.GET['location1'],location2=request.GET['location2'],departuredate=request.GET['departuredate'])
    return render(request,'train/availabletrain.html',{'trains':trains})

@login_required
def payment(request,train_id):
    train=get_object_or_404(Train,pk=train_id)
    return render(request,'train/payment.html',{'train':train})

