from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class SignUpForm(UserCreationForm):

    phone = models.CharField(verbose_name='email', max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']