from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import EmailField
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Profile


class SignUpForm(UserCreationForm):
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs = {'placeholder': 'email'}))
    password1=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'repeat password'}))
    class Meta:
        model=User
        
        fields=['username','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'username'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email'] 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number','image','birth_date']