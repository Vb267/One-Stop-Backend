# onestop_app/views.py

from django.shortcuts import render
#Each of these functions are used for handling HTTP requests of the landing page
def landing_page(request):
    return render(request, 'landing_page.html')

def networking_page(request):
    return render(request, 'networking_page.html')

def mentorship_page(request):
    return render(request, 'mentorship_page.html')

def resources_page(request):
    return render(request, 'resources_page.html')

def jobsinternships_page(request):
    return render(request, 'jobsinternships_page.html')
