from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views



urlpatterns = [
   path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('user_list/', views.user_list, name='user_list'),
    
    path('alumni_registration/', views.alumni_registration, name='alumni_registration'),
    path('student_registration/', views.student_registration,name='student_registration'),
    path('admin_registration/', views.admin_registration, name='admin_registration'),
   


]
