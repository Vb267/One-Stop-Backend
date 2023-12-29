from django.shortcuts import render
from rest_framework import viewsets
from Networking.models import Alumni_Profile

def mentorship_view(request):
    # Your mentorship view logic
    return render(request, 'mentorship.html')
