from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('newEmployeeform/',newEmployeeform,name='newEmployeeform'),
    
    path('saveuser/',saveuser, name='saveuser'),
    path('employeelist/',employeelist, name='employeelist'),
    path('updateEmployee/',updateEmployee,name='updateEmployee'),
    path('deleteEmployee/',deleteEmployee,name='deleteEmployee'),
    path('updateEmployeeform/',updateEmployeeform,name='updateEmployeeform'),
    
]