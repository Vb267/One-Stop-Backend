from django.contrib import admin
from django.urls import path,include
from SignUp.views import Student_ProfileViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'signup',Student_ProfileViewSet)

urlpatterns = [
   path('',include(router.urls))
   


]
