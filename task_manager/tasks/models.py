from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User


# Create your models here
class Task(models.Model):
    name = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='Status')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Author')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Executor')
    date_created = models.DateTimeField(auto_now_add=True)
