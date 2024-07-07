from django.urls import path
from . import views

app_name = 'mechanic'

urlpatterns=[

    path('', views.dashboard, name='dashboard'),

]