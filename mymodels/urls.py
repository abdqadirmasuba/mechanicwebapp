from django.urls import path
from . import views


app_name = 'mymodels'

urlpatterns=[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('accounts/login/', views.login_view, name='login_view'),
]