from django.shortcuts import render,get_object_or_404
from .models import Cab
# Create your views here.
def cab(request):
    return render(request,'cab/cab.html')

#passes only cab whose available field is tickmarked
def availablecab(request):
    cabs=Cab.objects.filter(available=True,location1=request.GET['location1'],location2=request.GET['location2'])
    return render(request,'cab/availablecab.html',{'cabs':cabs})

#will it call the function cab? check. If not then in flights do flight in payment section
def payment(request,cab_id):
    cab=get_object_or_404(Cab,pk=cab_id)
    return render(request,'cab/payment.html',{'cab':cab})