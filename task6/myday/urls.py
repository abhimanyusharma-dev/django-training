from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('creatproduct/', createproduct, name='createproduct'),
    path('productlist/', productlist, name='productlist'),
    path('updateProduct/', updateProduct, name='updateProduct'),
    path('deleteProduct/', deleteProduct, name='deleteProduct'),
    path('newproductform/',newproductform,name='newproductform'),
]