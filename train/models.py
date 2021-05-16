from django.db import models  

# Create your models here.
class Train(models.Model):
    location1=models.CharField(max_length=100)
    location2=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    departuredate=models.DateField()    
    returndate=models.DateField(blank=True)
    departuretime=models.TimeField()
    arrivaltime=models.TimeField()
    duration=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    available=models.BooleanField(default=True)


    def __str__(self):
        return self.location1
