from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from SignUp.models import Student_Profile, Alumni_Profile, Admin_Profile
from django.shortcuts import render
from rest_framework import viewsets
from SignUp.serializers import SignUp_Serializers


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        profile_type = request.POST.get('profile_type')

        if profile_type == 'Student':
            with transaction.atomic():
                student_profile = Student_Profile.objects.create()
            return JsonResponse({'message': 'Student profile created.'})

        elif profile_type == 'Alumni':
            with transaction.atomic():
                alumni_profile = Alumni_Profile.objects.create()
            return JsonResponse({'message': 'Alumni profile created.'})

        elif profile_type == 'Admin':
            with transaction.atomic():
                admin_profile = Admin_Profile.objects.create()
            return JsonResponse({'message': 'Admin profile created.'})

    return JsonResponse({'message': 'Invalid request.'})

class Student_ProfileViewSet(viewsets.ModelViewSet):
    queryset=Student_Profile.objects.all()
    serializer_class=SignUp_Serializers
