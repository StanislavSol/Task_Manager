from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django import forms

MIN_LENGTH_PASS = 3


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]


class UserEditForm(forms.ModelForm):
    error_messages = {
            'password_mismatch': _("The two password fields didn't match."),
            'password_length': _("The entered password is too short. It must contain at least 3 characters."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput,
        help_text=_("Your password must contain at least 3 characters."))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("To confirm, please enter your password again."))

    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'username',
                ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if len(password2) < MIN_LENGTH_PASS:
            raise forms.ValidationError(
                self.error_messages['password_length'],
                code='password_length',
            )
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
