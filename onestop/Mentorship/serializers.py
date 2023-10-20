#Create Serializers here
from rest_framework import serializers
from Networking.models import Student_Profile

class MentorshipSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model:Student_Profile
    fields:'all'
