from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from re import fullmatch


class User(models.Model):
    first_name = models.CharField(max_length=150,  default='', null=False,  blank=False)
    last_name = models.CharField(max_length=200, default='', null=False,  blank=False)
    username = models.CharField(max_length=150,
                                default='',
                                null=False,
                                blank=False,
                                unique=True,
                                help_text=_('Obligatory field. No more than 150 characters. \
                                             Only letters, numbers and symbols @/./+/-/_.'))
    password = models.CharField(max_length=50, default='', null=False,  blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False,  blank=False)

    def check_username(self):
        username_patern = '\w+[@/./+/-/]*'
        cd = self.cleaned_data
        if fullmatch(username_patern, cd["username"]) is None:
            raise forms.ValidationError(_('Please enter a correct username. It can only contain letters, numbers and @/./+/-/_.'))
        return cd['username']
