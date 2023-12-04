from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from .models import Task
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .filters import TasksFilter
from django_filters.views import FilterView

class TaskMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    success_url = reverse_lazy("tasks")
    login_url = reverse_lazy('login')
    fields = ['name', 'description', 'status', 'executor', 'labels']


class ListTasks(TaskMixin, FilterView):
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'
    filterset_class = TasksFilter
 #   filter_backends = [DjangoFilterBackend]
 #   filter_fields = ['status', 'executor', 'lables']


class CreateTask(TaskMixin, CreateView):
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(TaskMixin, UpdateView):
    template_name = "tasks/update.html"
    success_message = _('Task successfully changed')


class DeleteTask(TaskMixin, DeleteView):
    template_name = "tasks/delete.html"
    context_object_name = 'task'
    success_message = _('Task successfully deleted')

    def has_permission(self):
        return self.get_object().author.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(self.request, _('Only its author can delete a task'))
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)


class TaskCard(TaskMixin, DetailView):
    context_object_name = 'task'
    success_url = 'tasks/task_detail.html'
