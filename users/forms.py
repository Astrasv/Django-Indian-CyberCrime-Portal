from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) # Note: required = True is default
    
    class Meta:
        model = User # Affects the User model
        fields = ['username','email','password1','password2'] # These field names there in inbuilt UserCreation class already
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True) # Note: required = True is default
    
    class Meta:
        model = User # Affects the User model
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']