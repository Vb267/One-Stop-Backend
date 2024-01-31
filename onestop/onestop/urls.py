from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/',admin.site.urls),
    path("signup/",include('SignUp.urls')),
    path('Chat/', include('Chat.urls')),
    path('mentorship/',include('Mentorship.urls')),
    path('networking/',include('Networking.urls')),
    path('landingpage/',include('Landing_Page.urls')),
    path('resources/',include('Resources.urls'))
]
