from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from .models import Status
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError


class StatusMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Status
    success_url = reverse_lazy("statuses")
    context_object_name = 'statuses'
    login_url = reverse_lazy('login')
    fields = ['name']


class ListStatuses(StatusMixin, ListView):
    template_name = "statuses/statuses_list.html"


class CreateStatus(StatusMixin, CreateView):
    template_name = "statuses/create.html"
    success_message = _('Status successfully created')


class UpdateStatus(StatusMixin, UpdateView):
    template_name = "statuses/update.html"
    success_message = _('Status successfully changed')


class DeleteStatus(StatusMixin, DeleteView):
    template_name = "statuses/delete.html"

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                    self.request,
                    _('Status successfully deleted')
                    )
            return redirect(reverse_lazy('statuses'))
        except ProtectedError:
            messages.error(
                    self.request,
                    _('Cannot delete status because it is in use')
                    )
            return redirect(reverse_lazy('statuses'))
