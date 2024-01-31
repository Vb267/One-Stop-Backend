from django.shortcuts import render
from rest_framework import viewsets
from Networking.models import Alumni

def mentorship_view(request):
    # Your mentorship view logic
    return render(request, 'mentorship.html')
