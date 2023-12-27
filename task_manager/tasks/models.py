from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Name')
        )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name=_('Status')
        )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name=_('Description')
        )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author')
        )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        verbose_name=_('Executor'),
        blank=True,
        null=True
        )

    labels = models.ManyToManyField(
        Label,
        through='TaskRelationLabel',
        blank=True,
        verbose_name=_('Labels')
        )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskRelationLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(
        Label,
        on_delete=models.PROTECT,
        null=True
        )
