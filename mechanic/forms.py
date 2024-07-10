from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from mymodels.models import Custom_User
from django import forms

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Custom_User
        fields = ("last_name", "email","first_name","profile")

        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'class': 'input-field','required':'required'}),
            'first_name': forms.TextInput(attrs={'class': 'input-field'}),
            'profile': forms.FileInput(attrs={'class': 'input-field'}),            
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add class attributes to individual input widgets
        self.fields['old_password'].widget.attrs.update({'class': 'input-field'})
        self.fields['new_password1'].widget.attrs.update({'class': 'input-field'})
        self.fields['new_password2'].widget.attrs.update({'class': 'input-field'})