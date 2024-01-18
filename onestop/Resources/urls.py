# Resources/urls.py
from django.urls import path
from .views import resource_list

urlpatterns = [
    path('types_of_resources/', resource_list, name='item-list'),
]