from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def facebook(request):
    f= "<h1>Welcome to facebook page</h1>"
    return HttpResponse(f)


def instagram(request):
    i= "<h1>Welcome to instagram page</h1>"
    return HttpResponse(i)