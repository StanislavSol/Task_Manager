import django_filters
from task_manager.tasks.models import Task
from django import forms
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class TasksFilter(django_filters.FilterSet):

    def show_your_tasks(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    your_tasks = django_filters.BooleanFilter(
        method='show_your_tasks',
        widget=forms.CheckboxInput,
        label=_('Only your tasks'),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label'),
        widget=forms.Select(
            attrs={'class': 'form-select'}
        )
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
