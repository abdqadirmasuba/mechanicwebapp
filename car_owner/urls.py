from django.urls import path
from . import views

app_name = 'car_owner'

urlpatterns=[

    path('', views.place_request, name='request'),

]