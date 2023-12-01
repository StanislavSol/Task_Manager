from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
