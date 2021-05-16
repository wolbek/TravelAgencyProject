from django.db import models

# Create your models here.
class Cab(models.Model):
    location1=models.CharField(max_length=100)
    location2=models.CharField(max_length=100)
    name=models.CharField(max_length=100) 
    image=models.ImageField(upload_to='cab/images')
    luggagebag=models.IntegerField()
    seat=models.IntegerField()
    price=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)    
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.location1

