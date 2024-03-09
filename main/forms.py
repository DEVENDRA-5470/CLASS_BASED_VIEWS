from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *
class myform(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email']


class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'