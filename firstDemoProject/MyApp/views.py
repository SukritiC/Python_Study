from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# the function must accept request and give a response- django view
def index(request):
    # view must return a proper HTTP response - hence imported the above HttpResponse
    return HttpResponse('Hello World')


# creating a view isn't sufficient - it must be associated with a URL pattern
# first create a new URL Pattern inside urls.py