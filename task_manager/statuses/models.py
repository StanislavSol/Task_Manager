from django.db import models
from django.utils import timezone

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(default=timezone.now(), verbose_name='date joined')
