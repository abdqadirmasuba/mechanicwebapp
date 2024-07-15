from mymodels.models import Request
from django import forms

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['car_model', 'car_number', 'phone_number', 'email', 'car_image']
        widgets = {
            'car_model': forms.TextInput(attrs={'class': 'form-control'}),
            'car_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'car_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }