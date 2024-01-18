# exampleapp/views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Resource

def resource_list(request):
    Resource_list = Resource.objects.all()

    # Number of items to display per page
    Resource_per_page = 10
    paginator = Paginator(Resource_list, Resource_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the specified page
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return render(request, 'types_of_resources.html', {'items': items})
