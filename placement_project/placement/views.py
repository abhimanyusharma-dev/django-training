from django.shortcuts import render, redirect
from django.contrib import messages
import joblib
from django.contrib.auth.hashers import (
    make_password,
    check_password
)

from .models import User
from .forms import (
    RegistrationForm,
    LoginForm,
    PredictionForm
)


# =========================
# HOME
# =========================

def home(request):

    return render(
        request,
        "home.html"
    )


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == "POST":

        form = RegistrationForm(
            request.POST
        )

        if form.is_valid():

            student_id = form.cleaned_data[
                "student_id"
            ]

            if User.objects.filter(
                student_id=student_id
            ).exists():

                messages.error(
                    request,
                    "Student ID already registered."
                )

            else:

                user = form.save(
                    commit=False
                )

                user.password = make_password(
                    form.cleaned_data["password"]
                )

                user.save()

                messages.success(
                    request,
                    "Registration successful!"
                )

                return redirect("login")

    else:

        form = RegistrationForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":

        form = LoginForm(
            request.POST
        )

        if form.is_valid():

            student_id = form.cleaned_data[
                "student_id"
            ]

            password = form.cleaned_data[
                "password"
            ]

            try:

                user = User.objects.get(
                    student_id=student_id
                )

                if check_password(
                    password,
                    user.password
                ):

                    request.session[
                        "student_id"
                    ] = user.student_id

                    request.session[
                        "student_name"
                    ] = user.name

                    return redirect(
                        "prediction"
                    )

                else:

                    messages.error(
                        request,
                        "Incorrect password."
                    )

            except User.DoesNotExist:

                messages.error(
                    request,
                    "Student ID not found."
                )

    else:

        form = LoginForm()

    return render(
        request,
        "login.html",
        {
            "form": form
        }
    )


# =========================
# PREDICTION PAGE
# =========================

def prediction(request):

    if "student_id" not in request.session:

        return redirect("login")

    form = PredictionForm()

    result = None

    if request.method == "POST":

        form = PredictionForm(
            request.POST
        )

        if form.is_valid():

            cgpa = form.cleaned_data["cgpa"]
            iq = form.cleaned_data["iq"]
            profile_score = form.cleaned_data[
                "profile_score"
            ]

            # ===================================
            # ML MODEL YAHAN BAAD ME LAGANA HAI
            # ===================================

            # Example:
            #
            # prediction = model.predict([
            #     [cgpa, iq, profile_score]
            # ])
            #
            # result = prediction[0]

            result = "Prediction will appear here"

    return render(
        request,
        "prediction.html",
        {
            "form": form,
            "result": result,
            "student_name": request.session.get(
                "student_name"
            )
        }
    )


# =========================
# LOGOUT
# =========================

def logout_view(request):

    request.session.flush()

    return redirect("home")


import os

from django.conf import settings



def result(request):

    scaler_path = os.path.join(
        settings.BASE_DIR,
        'student_scalar.pkl'
    )

    model_path = os.path.join(
        settings.BASE_DIR,
        'student_mlmodel.pkl'
    )

    scaler = joblib.load(scaler_path)
    mlmodel = joblib.load(model_path)

    lis = []

    lis.append(float(request.GET['CGPA']))
    lis.append(float(request.GET['IQ']))
    lis.append(float(request.GET['Profile']))

    scaled_input = scaler.transform([lis])

    ans = mlmodel.predict(scaled_input)[0]

    res = render(
        request,
        'result.html',
        {
            'ans': ans,
            'lis': lis
        }
    )

    return res