from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        help_text="Необходимо. Введите имя пользователя",
    )
    email = forms.CharField(
        max_length=30,
        required=True,
        help_text="Необходимо. Введите свой email",
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    pass
