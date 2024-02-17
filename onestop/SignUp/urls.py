# SingUp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomUserViewSet, AlumniViewSet, StudentViewSet, AdminViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'alumni', AlumniViewSet)
router.register(r'students', StudentViewSet)
router.register(r'admins', AdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
