from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = [
        'first_name', 'last_name', 'email',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}'s custom account"
