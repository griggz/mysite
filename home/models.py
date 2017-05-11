from django.db import models
from django.conf import settings


# Create your models here.
class Feedback(models.Model):
    comments = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-id"]
