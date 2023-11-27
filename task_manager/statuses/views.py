from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views import View
from .models import Status
from .forms import StatusForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ListStatuses(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/statuses_list.html"
    context_object_name = 'statuses'


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy("statuses")
    success_message = _('Status successfully created')


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses")
    success_message = _('Status successfully changed')


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = "statuses/delete.html"
    context_object_name = 'status'
    success_url = reverse_lazy("statuses")
    success_message = _('Status successfully deleted')
