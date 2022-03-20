from django.db import models
from accounts.models import Account
# Create your models here.
class RequestArticle(models.Model):
    title = models.CharField(max_length=100,null=False)
    content = models.TextField(null=False)
    requestImage = models.ImageField(null=False,upload_to="")
    writer = models.ForeignKey(Account,on_delete=models.CASCADE,null=False)