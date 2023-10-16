from django.db import models

# Create your models here.
class CustDetails(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField(max_length=254)
  phnum=models.PhoneNumberField(_null=False,max_length=12,unique=True,blank=False)
  