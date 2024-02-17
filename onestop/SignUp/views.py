# accounts/views.py
from .models import CustomUser,Alumni, Student, Admin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm,AlumniForm, StudentForm, AdminForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'message': 'Login successful!'})
    else:
        form = CustomAuthenticationForm()
    return JsonResponse({'error': 'Invalid request method'})

def user_list(request):
    users = CustomUser.objects.all()
    user_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return JsonResponse({'users': user_data})

def home_view(request):
    return JsonResponse({'message': 'Welcome to the home page!'})

@api_view(['POST'])
def signup_view(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return Response({'message': 'User registration successful!'})
    else:
        return Response(form.errors, status=400)

@api_view(['POST'])
def alumni_registration(request):
    form = AlumniForm(request.POST)
    if form.is_valid():
        alumni = form.save(commit=False)
        alumni.user = request.user
        alumni.save()
        return Response({'message': 'Alumni registration successful!'})
    else:
        return Response(form.errors, status=400)

@api_view(['POST'])
def student_registration(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        student = form.save(commit=False)
        student.user = request.user
        student.save()
        return Response({'message': 'Student registration successful!'})
    else:
        return Response(form.errors, status=400)

@api_view(['POST'])
def admin_registration(request):
    form = AdminForm(request.POST)
    if form.is_valid():
        admin = form.save(commit=False)
        admin.user = request.user
        admin.save()
        return Response({'message': 'Admin registration successful!'})
    else:
        return Response(form.errors, status=400)