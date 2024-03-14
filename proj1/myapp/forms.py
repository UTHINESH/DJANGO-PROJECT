from django.forms import ModelForm
from .models import User as user1

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput

from django import forms

class UserFrom(ModelForm):

    class Meta:

        model = user1
        fields ='__all__'


class CreateUserForm(UserCreationForm):

    class Meta:

        model= User
        fields=['username','email','password1','password2']


class Loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
