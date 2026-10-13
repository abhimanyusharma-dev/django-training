from django.shortcuts import render
from myday.models import product
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def newproductform(request):
    res = render(request,'newproductform.html')
    return res


def createproduct(request): 
    # C for Create
    p_id= request.POST['p_id']
    p_name = request.POST['p_name']
    p_price = request.POST['p_price']
    p_offer = request.POST['p_offer']
    pro = product(p_id=p_id,p_name=p_name,p_price=p_price,p_offer=p_offer)
    pro.save()
    url = reverse('productlist')
    return HttpResponseRedirect(url)


def productlist(request):
    Products = product.objects.all() # read data records ......R for Read
    # It returns query set
    res = render(request,'productlist.html', {'Products':Products})
    return res



def updateProduct(request):
    id=2
    p_id=102
    p_price=100000
    p_name='Apple Mackbook'
    p_offer=17.5
    product(id=id,p_id=p_id,p_price=p_price,p_name=p_name,p_offer=p_offer).save()
    return HttpResponse('<h1>product is Updated successfully</h1>')


def deleteProduct(request):
    id=3
    emp=product.objects.filter(id=id)
    emp.delete()
    return HttpResponse('<h1>product is deleted successfully</h1>')