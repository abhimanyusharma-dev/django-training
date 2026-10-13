from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from database.models import employee
from django.urls import reverse

# Create your views here.

def newEmployeeform(request):
    res= render(request ,'newEmployeeform.html')
    return res




def saveuser(request): 
    # C for Create
    eno = request.POST['eno']
    ename = request.POST['ename']
    esal = request.POST['esal']
    emp = employee(eno=eno,ename=ename,esal=esal)
    emp.save()
    url= reverse('employeelist')
    return HttpResponseRedirect(url)


def employeelist(request):
    Employees = employee.objects.all() # read data records ......R for Read
    # It returns query set
    res = render(request,'employeelist.html', {'Employees':Employees})
    return res


def updateEmployeeform(request):
    id=request.GET['id']
    Employee=employee.objects.filter(id=id).values()
    res =render(request, 'updateEmployeeform.html',{'Employee':Employee[0]})
    return res
    
def updateEmployee(request):
    id=request.POST['id']
    eno=request.POST['eno']
    ename=request.POST['ename']
    esal=request.POST['esal']
    employee(id=id,eno=eno,ename=ename,esal=esal).save()
    url= reverse('employeelist')
    return HttpResponseRedirect(url)


def deleteEmployee(request):
    id=request.GET['id']
    emp=employee.objects.filter(id=id)
    emp.delete()
    url= reverse('employeelist')
    return HttpResponseRedirect(url)
    
    
    
    
    
    

    