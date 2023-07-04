from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    name = forms.CharField()
    mobile_number = forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'mobile_number', 'password1', 'password2']

