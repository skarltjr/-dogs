from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Account(AbstractUser):
    name = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=20,null=False)