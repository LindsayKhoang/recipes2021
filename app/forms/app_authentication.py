from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class AppAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Enter...",
                "class": "form-control form-control-user",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control form-control-user",
                "placeholder": "Enter...",
            }
        ),
    )
