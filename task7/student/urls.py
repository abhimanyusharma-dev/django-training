from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('login/', views.login_view, name='login'),

    path('student/', views.student_form, name='student_form'),

    path('success/', views.success, name='success'),
]