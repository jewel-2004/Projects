from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields = ['name','email','course']  # fields = ['__all__']




class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
        
        