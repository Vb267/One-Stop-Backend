from django.db import models
from Networking.models import Alumni_Profile,Student_Profile #Imported profiles from Networking 

class Company_details(models.Model):
  cname=models.CharField(max_length=100)
  compid=models.AutoField(primary_key=True,max_digits=3)
  designation=models.CharField(max_length=100)
  package=models.BigIntegerField(max_length=20)
  job_description=models.TextField()
  process=models.TextField()
  employment_type=models.CharField(max_length=20)# Full-time, Part-time, Hybrid, Internship
  eligibility=models.TextField()
  