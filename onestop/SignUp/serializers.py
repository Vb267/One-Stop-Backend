from rest_framework import serializers
from SignUp.models import Student_Profile, Admin_Profile, Alumni_Profile

class SignUp_Serializers(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=Student_Profile
    fields="__all__"

    