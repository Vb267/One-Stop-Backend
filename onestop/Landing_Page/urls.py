from django.urls import path
from . import views

urlpatterns = [
    path('landing_page/', views.landing_page_view, name='landing_page'),
    # Add other landing page-related URLs
]
