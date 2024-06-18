from django.contrib.auth.models import AbstractUser
from django.db import models

class NewUser(AbstractUser):
    home_address = models.TextField(blank=True)
    favourite_facility = models.CharField(max_length=255, blank=True)

    REQUIRED_FIELDS = ['home_address']

    def __str__(self):
        return self.username
