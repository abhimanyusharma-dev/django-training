from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader

# Create your views here.

def testpaper(request):
      que ="who developed python?"
      a = "Guido van Rossum"
      b = "Elon Musk"
      c = "Bill Gates"
      d = "Mark Zuckerberg"
      context = {'question': que, 'option1': a, 'option2': b, 'option3': c, 'option4': d}
      template = loader.get_template('test_paper.html')
      res=template.render(context, request)
      return HttpResponse(res)
    
    
def info(request):
      que ="Abhimanyu sharma"
      a = "aids dept"
      b = "23"
      
      context = {'question': que, 'option1': a, 'option2': b, }
      template = loader.get_template('info.html')
      res=template.render(context, request)
      return HttpResponse(res)
    
    
def add(request):
      a = 10
      b = 20
      c = a + b
      context = {'num1': a, 'num2': b, 'results': c}
      template = loader.get_template('add.html')
      res=template.render(context, request)
      return HttpResponse(res)
    
    
    
def result(request):
      context={
        'name': 'John Doe',
        'Marks': 80
        
      }
      
      res=render(request, 'result.html', context)
      return HttpResponse(res)



def vote(request):
      context={
        'name': 'John Doe',
        'vote': 18,
        'contry': 'India'
        
      }
      
      res=render(request, 'vote.html', context)
      return HttpResponse(res)



def  home(request):
      return render(request, 'home.html')


def  about(request):
      return render(request, 'about.html')


def  contact(request):
      return render(request, 'contect.html')
