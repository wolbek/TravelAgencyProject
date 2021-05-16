from django.urls import path
from . import views

app_name='cab1'

urlpatterns = [    
    path('',views.cab,name='cab'),
    path('availablecab/',views.availablecab,name='availablecab'),
    path('<int:cab_id>',views.payment,name='payment')
]