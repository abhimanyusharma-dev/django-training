from django.shortcuts import render, redirect
from .models import User, Student
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'student/home.html')


def signup(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        User.objects.create(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'student/signup.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            return redirect('student_form')

        else:
            return render(
                request,
                'student/login.html',
                {'error': 'Invalid username or password'}
            )
        
    return render(request, 'student/login.html')


def student_form(request):

    if request.method == 'POST':

        sid = request.POST['sid']
        sname = request.POST['sname']
        sbranch = request.POST['sbranch']

        Student.objects.create(
            sid=sid,
            sname=sname,
            sbranch=sbranch
        )

        return redirect('success')

    return render(request, 'student/student_form.html')


def success(request):
    return render(request, 'student/success.html')



def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))