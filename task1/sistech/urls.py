from django.urls import path
from sistech import views

urlpatterns = [
    path('sistech/', views.sistech),
]