from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .mixins import RulesMixin
from .forms import UserCreation, UserChange


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserCreation
    success_url = reverse_lazy("login")
    template_name = "users/create.html"
    success_message = _('User successfully created')


class ListUsers(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = 'users'


class UpdateUser(RulesMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserChange
    template_name = "users/update.html"
    success_url = reverse_lazy("users")
    success_message = _('User successfully changed')


class DeleteUser(RulesMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    context_object_name = 'user'
    success_url = reverse_lazy("users")
    success_message = _('User successfully deleted')
