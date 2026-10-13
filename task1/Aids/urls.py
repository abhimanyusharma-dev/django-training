from django.urls import path
from Aids import views

urlpatterns = [
    path('aids/', views.aids),
]