from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shop_post_set')
    content = models.TextField(verbose_name="내용")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)