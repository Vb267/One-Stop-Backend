
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('alumni', 'Alumni'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

class Alumni(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    passout_year = models.IntegerField()
    company = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()
    date_of_birth = models.DateField()
    area_of_interest = models.CharField(max_length=100)  # You may want to consider using a ManyToManyField

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

