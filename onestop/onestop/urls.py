from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/',admin.site.urls),
    path("SignUp/v1/",include('SignUp.urls'))
]
