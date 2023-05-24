from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

CLASS_INPUT = "w-full py-4 px-6 rounded-xl"


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your username",
                "class": CLASS_INPUT,
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
                "class": CLASS_INPUT,
            }
        )
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your usarname",
                "class": CLASS_INPUT,
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email",
                "class": CLASS_INPUT,
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
                "class": CLASS_INPUT,
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm your password",
                "class": CLASS_INPUT,
            }
        )
    )
