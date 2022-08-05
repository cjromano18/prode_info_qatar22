from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.
class Usuario(AbstractUser):
    telefono=models.CharField(max_length=255, null=True, blank=True)
