from django.contrib.auth.models import AbstractUser
from django.db import models

class NewUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username
