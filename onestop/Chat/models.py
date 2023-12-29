from django.db import models

# Create your models here.
class Room(models.Model):
  name=models.CharField(max_length=1000)
  
class Message(models.Model):
  value=models.CharField(max_length=10000)
  date=models.DateTimeField(default=models.DateTimeField((""), auto_now=False, auto_now_add=False))
  user=models.CharField(max_length=10000)
  room=models.CharField(max_length=10000)