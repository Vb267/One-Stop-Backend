from django.urls import HttpResponse

def home_page(request):
  print("homepage requested")
  return HttpResponse()