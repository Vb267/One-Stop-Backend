from django.db import models
from Mentorship.models import MentorRating

class Student_Profile(models.Model):
  studid=models.AutoField(primary_key=True)
  fname=models.CharField(max_length=50)
  mname=models.CharField(max_length=50)
  lname=models.CharField(max_length=50)
  emailid=models.EmailField(max_length=254)
  phnum=models.PhoneNumberField( null=False,max_length=12,unique=True,blank=False)
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
  phnum=models.PhoneNumberField( null=False,max_length=12,unique=True,blank=False)
  about=models.TextField()
  dob=models.DateField((""), auto_now=False, auto_now_add=False)
  company=models.CharField(max_length=50)#Current Company
  sctc=models.IntegerField(max_length=10)#Starting CTC
  cctc=models.BigIntegerField(max_length=20)#Current CTC
  aoe=models.CharField(max_length=50)#Area of Expertise 
  rating=models.ForeignKey(MentorRating,on_delete=models.CASCADE)  #rating of alumni Imported from Mentorship

class Admin_Profile(models.Model):
  fname=models.CharField(max_length=50)
  mname=models.CharField(max_length=50)
  lname=models.CharField(max_length=50)
  emailid=models.EmailField(max_length=254)
  phnum=models.PhoneNumberField(null=False,max_length=12,unique=True,blank=False)

#class Connections(models.Model):
#class Chat_Feature(models.Model):
