from django.urls import path
from . import views

app_name='flight1'

urlpatterns = [    
    path('',views.flight,name='flight'),
    path('availableflight/',views.availableflight,name='availableflight'),
    path('<int:flight_id>',views.payment,name='payment')
]