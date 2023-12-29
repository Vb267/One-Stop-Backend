from django.contrib import admin
from django.urls import path
from rest_framework import routers


from django.urls import path
from . import views

urlpatterns = [
    path('mentorship/', views.mentorship_view, name='mentorship'),
    # Add other networking-related URLs
]
