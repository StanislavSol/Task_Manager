from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150)
    full_name = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
