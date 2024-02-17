# accounts/views.py
from .models import CustomUser,Alumni, Student, Admin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm,AlumniForm, StudentForm, AdminForm
from django.http import JsonResponse

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

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Redirect to the appropriate registration page based on user type
            if user.user_type == 'alumni':
                return JsonResponse({'message': 'Alumni registration successful!'})
            elif user.user_type == 'student':
                return JsonResponse({'message': 'Student registration successful!'})
            elif user.user_type == 'admin':
                return JsonResponse({'message': 'Admin registration successful!'})
    else:
        form = CustomUserCreationForm()
    return JsonResponse({'error': 'Invalid request method'})

def alumni_registration(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            alumni = form.save(commit=False)
            alumni.user = request.user
            alumni.save()
            return JsonResponse({'message': 'Alumni registration successful!'})
    else:
        form = AlumniForm()
    return JsonResponse({'error': 'Invalid request method'})

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return JsonResponse({'message': 'Student registration successful!'})
    else:
        form = StudentForm()
    return JsonResponse({'error': 'Invalid request method'})

def admin_registration(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
            return JsonResponse({'message': 'Admin registration successful!'})
    else:
        form = AdminForm()
    return JsonResponse({'error': 'Invalid request method'})