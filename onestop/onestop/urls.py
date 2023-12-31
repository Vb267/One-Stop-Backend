from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/',admin.site.urls),
    path("SignUp/v1/",include('SignUp.urls')),
    path('Chat/', include('Chat.urls')),
    path('mentorship/',include('Mentorship.urls')),
    path('networking/',include('Networking.urls')),
    path('landingpage/',include('Landing_Page.urls'))
]
