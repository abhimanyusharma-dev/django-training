from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shopping(request):
    return render(request, 'shopping.html')