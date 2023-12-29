from django.urls import path
from . import views

urlpatterns = [
    path('networking/', views.networking_view, name='networking'),
    # Add other networking-related URLs
]
