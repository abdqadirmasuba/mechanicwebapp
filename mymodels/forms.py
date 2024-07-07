from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.gis.geos import Point
from django.contrib.gis import forms as gis_forms
from .models import User, Mechanic


class MechanicRegistrationForm(UserCreationForm):
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    vehicles_of_expertise = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    work_hours = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'experience', 'vehicles_of_expertise', 'location', 'work_hours')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }