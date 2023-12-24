from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import logout


class LogIn(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('You are logged in')


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out'))
    return redirect('index')
