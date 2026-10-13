from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def test_paper(request):
    template = loader.get_template('test_paper.html')
    res=template.render()
    return HttpResponse(res)