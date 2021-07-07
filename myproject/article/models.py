from django.db import models
from django.urls import reverse

# Create your models here.
STATUS_CHOICES = (
    ('d','Draft'),
    ('p','Published'),
    ('w','Withdrawn'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    photo = models.ImageField(blank=True, upload_to='article%Y/%m/%d') # 필드별로 다른 디렉터리저장+시간대

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.id])