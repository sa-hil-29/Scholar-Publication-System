from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=100, label='Full Name')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name']
