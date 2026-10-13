from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aids(request):
    h1= "<h1>Welcome to Aids page</h1>"
    h2= "<h2>Welcome to Aids page</h2>"
    return HttpResponse(h1 + h2)