from django.contrib.auth.models import User
from django.db import models


class Beeps(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

