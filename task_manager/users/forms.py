from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from task_manager.users.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


PASS_WIDGET = forms.PasswordInput()


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            ]


class UserChange(UserChangeForm):
    password = None

    password1 = forms.CharField(
        label=_('Password'),
        widget=PASS_WIDGET,
        help_text=_('Your password must be at least 3 characters long.'),
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=PASS_WIDGET,
        help_text=_('To confirm, please enter your password again.'),
    )

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2
