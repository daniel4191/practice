from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# code line

class UserForm(UserCreationForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('username', 'email')
