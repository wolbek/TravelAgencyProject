from django.urls import path
from . import views

app_name='train1'

urlpatterns = [    
    path('',views.train,name='train'),
    path('availabletrain/',views.availabletrain,name='availabletrain'),
    path('<int:train_id>',views.payment,name='payment')
]