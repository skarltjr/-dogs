import os
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from accounts.models import Account
# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=100,null=False)
    content = models.TextField(null=False)
    reportImage = models.ImageField(null=False,upload_to="")
    writer = models.ForeignKey(Account,on_delete=models.CASCADE,null=False)