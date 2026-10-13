from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter password"
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password"
            }
        )
    )

    class Meta:

        model = User

        fields = [
            "student_id",
            "name",
            "mobile",
            "branch",
            "password"
        ]

        widgets = {

            "student_id": forms.TextInput(
                attrs={
                    "placeholder": "Enter Student ID"
                }
            ),

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter Full Name"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "placeholder": "Enter Mobile Number"
                }
            ),

            "branch": forms.TextInput(
                attrs={
                    "placeholder": "Enter Branch"
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get(
            "password"
        )

        confirm_password = cleaned_data.get(
            "confirm_password"
        )

        if password and confirm_password:

            if password != confirm_password:

                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data


class LoginForm(forms.Form):

    student_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Student ID"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password"
            }
        )
    )


class PredictionForm(forms.Form):

    cgpa = forms.FloatField(
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter CGPA",
                "step": "0.01"
            }
        )
    )

    iq = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter IQ"
            }
        )
    )

    profile_score = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter Profile Score",
                "step": "0.01"
            }
        )
    )