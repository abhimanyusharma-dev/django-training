from django.urls import path
from myapp1 import views

urlpatterns = [
    path('test-paper/', views.test_paper),
]