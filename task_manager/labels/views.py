from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from task_manager.labels.models import Label
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError


class LabelsMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Label
    success_url = reverse_lazy("labels")
    context_object_name = 'labels'
    login_url = reverse_lazy('login')
    fields = ['name']


class ListLabels(LabelsMixin, ListView):
    template_name = "labels/labels_list.html"


class CreateLabel(LabelsMixin, CreateView):
    template_name = "labels/create.html"
    success_message = _('Label successfully created')


class UpdateLabel(LabelsMixin, UpdateView):
    template_name = "labels/update.html"
    success_message = _('Label successfully changed')


class DeleteLabel(LabelsMixin, DeleteView):
    template_name = "labels/delete.html"

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                self.request,
               _('Label successfully deleted')
            )
            return redirect(reverse_lazy('labels'))
        except ProtectedError:
            messages.error(
                self.request,
                _('Cannot delete label because it is in use')
            )
            return redirect(reverse_lazy('labels'))
