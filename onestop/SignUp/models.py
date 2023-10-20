from django.db import models

# Create your models here.

class ProfileChoice(models.Model):
    PROFILE_CHOICES = (
        ('Student', 'Student'),
        ('Alumni', 'Alumni'),
        ('Admin', 'Admin'),
    )
    profile_type = models.CharField(
        max_length=10,
        choices=PROFILE_CHOICES,
        default='Student',
    )

class Student_Profile(models.Model):
  studid=models.AutoField(primary_key=True)
  fname=models.CharField(max_length=50)
  mname=models.CharField(max_length=50)
  lname=models.CharField(max_length=50)
  emailid=models.EmailField(max_length=254)
  phnum=models.CharField(max_length=10)
  about=models.TextField()
  dob=models.DateField((""), auto_now=False, auto_now_add=False)
  class_year=models.CharField(max_length=10)
  branch=models.CharField(max_length=50)
  domain=models.CharField(max_length=50)

class Alumni_Profile(models.Model):
  alumniid=models.AutoField(primary_key=True)
  fname=models.CharField(max_length=50)
  mname=models.CharField(max_length=50)
  lname=models.CharField(max_length=50)
  emailid=models.EmailField(max_length=254)
  phnum=models.CharField(max_length=10)
  about=models.TextField()
  dob=models.DateField((""), auto_now=False, auto_now_add=False)
  company=models.CharField(max_length=50)#Current Company
  sctc=models.IntegerField(max_length=10)#Starting CTC
  cctc=models.BigIntegerField(max_length=20)#Current CTC
  aoe=models.CharField(max_length=50)#Area of Expertise 
  

class Admin_Profile(models.Model):
  fname=models.CharField(max_length=50)
  mname=models.CharField(max_length=50)
  lname=models.CharField(max_length=50)
  emailid=models.EmailField(max_length=254)
  phnum=models.CharField(max_length=10)

