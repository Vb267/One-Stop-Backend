# SignUp/serializers.py
from rest_framework import serializers
from .models import CustomUser, Alumni, Student, Admin

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'user_type']

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        exclude = ['user']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['user']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        exclude = ['user']
