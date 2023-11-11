from django import forms
from django.db import models
from task_manager.users.models import User
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from re import fullmatch


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(help_text=_('Your password must contain \
                                             at least 3 characters.'))
    password2 = forms.CharField(help_text=_('To confirm, please\
                                             enter your password again.'),
                                validators=[MinLengthValidator(
                                           limit_value=3,
                                           message=_(
                                            'The entered password is too short. \
                                            It must contain at least 3 characters.'
                                             ))])
    class Meta:
        model = User
        fields = (
                'first_name',
                'last_name',
                'username',
                'password1',
                'password2'
                )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_('The entered passwords do not match.'))
        return cd['password2']

    def check_username(self):
        username_patern = '[\w@/./+/-/]+'
        cd = self.cleaned_data
        if fullmatch(username_patern, cd["username"]) is None:
            raise forms.ValidationError(_('Please enter a correct username. It can only contain letters, numbers and @/./+/-/_.'))
        return cd['username']
