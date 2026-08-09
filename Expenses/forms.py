from django import forms
from django.contrib.auth.models import User
from .models import expenses
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreation(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model=User
        fields=['username','email']
        
class MainExpenses(forms.ModelForm):
    class Meta:
        model=expenses
        fields=['title','amount','category','date','description']