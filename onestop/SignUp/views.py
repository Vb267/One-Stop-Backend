# accounts/views.py
from .models import CustomUser,Alumni, Student, Admin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm,AlumniForm, StudentForm, AdminForm




def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change 'home' to your desired home page
    else:
        form = CustomAuthenticationForm()
    return render(request, 'signup/login.html', {'form': form})

# accounts/views.py



def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'signup/user_list.html', {'users': users})


def home_view(request):
    return render(request, 'signup/home.html')  # Replace 'accounts/home.html' with your actual template path



# accounts/views.py



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Redirect to the appropriate registration page based on user type
            if user.user_type == 'alumni':
                return redirect('alumni_registration')
            elif user.user_type == 'student':
                return redirect('student_registration')
            elif user.user_type == 'admin':
                return redirect('admin_registration')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

def alumni_registration(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            alumni = form.save(commit=False)
            alumni.user = request.user
            alumni.save()
            return redirect('home')  # Change 'home' to your desired home page
    else:
        form = AlumniForm()
    return render(request, 'signup/alumni_registration.html', {'form': form})

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('home')  # Change 'home' to your desired home page
    else:
        form = StudentForm()
    return render(request, 'signup/student_registration.html', {'form': form})

def admin_registration(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
            return redirect('home')  # Change 'home' to your desired home page
    else:
        form = AdminForm()
    return render(request, 'signup/admin_registration.html', {'form': form})
