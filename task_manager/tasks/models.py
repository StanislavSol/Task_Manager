from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User


# Create your models here
class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)

    status = models.ForeignKey(Status,
            on_delete=models.PROTECT,
            related_name='Status')

    description = models.TextField(max_length=500, blank=True, null=True)

    author = models.ForeignKey(User,
            on_delete=models.PROTECT,
            related_name='Author')

    executor = models.ForeignKey(
            User,
            on_delete=models.PROTECT,
            related_name='Executor',
            blank=True,
            null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
