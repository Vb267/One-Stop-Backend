# onestop/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm

#Each of these functions are used for handling HTTP requests of the landing page
def landing_page(request):
    return render(request, 'landing_page.html')
    signup_url = reverse('signup')
    login_url = reverse('login')

    return render(request, 'landing_page.html', {'signup_url': signup_url, 'login_url': login_url})

def signup(request):
    # Add code for sign-up logic here
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Add code to create a user account and perform any necessary actions
            # For example, you can use Django's User model to create a new user.
            # Don't forget to hash and store the password securely.
            
            # After successful registration, you can redirect the user to a login page or home page.
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login(request):
    # Add code for login logic here
    return render(request, 'login.html')





def networking_page(request):
    return render(request, 'networking_page.html')

def mentorship_page(request):
    return render(request, 'mentorship_page.html')

def resources_page(request):
    return render(request, 'resources_page.html')

def jobsinternships_page(request):
    return render(request, 'jobsinternships_page.html')
