from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cse(request):
    h1= "<h1>Welcome to CSE page</h1>"
    h2= "<h2>Welcome to CSE page</h2>"
    return HttpResponse(h1 + h2)