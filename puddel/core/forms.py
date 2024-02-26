from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

class LoginForm(AuthenticationForm):
     username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    
     password= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))         
    



class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')

    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    

    email= forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    

    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    

    password2= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat pass',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    