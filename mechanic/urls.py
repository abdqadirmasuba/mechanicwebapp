from django.urls import path
from . import views
from .views import RequestPasswordResetEmail, PasswordReset
from django.contrib.auth import views as auth_views


app_name = 'mechanic'

urlpatterns=[

    path('', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('read_all_notifications/', views.read_all_notifications, name='read_all_notifications'),
    path('password-update/', views.password_update, name='password_update'),
    path('user-info-update/', views.user_info_update, name='user_info_update'),
    path(r'set-new-password/<uidb64>/<token>',PasswordReset.as_view(),name='new-password'),
    path(r'password-reset',RequestPasswordResetEmail.as_view(),name="password-reset"),

]