# onestop/urls.py

from django.urls import path
from . import views
#URL patterns are given below to switch from one page to another
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('networking/', views.networking_page, name='networking_page'),
    path('mentorship/', views.mentorship_page, name='mentorship_page'),
    path('resources/', views.resources_page, name='resources_page'),
    path('jobsinternships/', views.jobsinternships_page, name='jobsinternships_page'),
    path('signup/', views.signup, name='signup'),
]
