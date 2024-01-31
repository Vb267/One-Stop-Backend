# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser,Alumni, Student, Admin

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser



class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        exclude = ('user',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user',)

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        exclude = ('user',)
