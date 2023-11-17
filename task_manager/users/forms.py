from django import forms
from .models import User
from django.contrib.auth.forms import (
                                       UserCreationForm,
                                       UserChangeForm
                                       )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'username'
                ]
