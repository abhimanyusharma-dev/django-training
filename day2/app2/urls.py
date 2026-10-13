from django.urls import path
from app2 import views

urlpatterns = [
    path('facebook/', views.facebook),
    path('instagram/', views.instagram), 
]