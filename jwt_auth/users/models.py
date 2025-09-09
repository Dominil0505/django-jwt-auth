from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class JWTUsers(AbstractUser):
    email = models.EmailField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)