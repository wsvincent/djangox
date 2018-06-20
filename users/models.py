from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add additional fields here. For example, a global-friendly name field
    # name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
