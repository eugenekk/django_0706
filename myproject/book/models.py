from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.

# 유효성 검사하는 애 추가
def numCheck(value):
    if not 1 <= value <= 10:
        raise ValidationError('판매 수량은 1~10 사이만 가능합니다.')


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=15) # 데이터를 등록한 client 의 ip를 insert하고 싶음(request 안에 들어있음 -> commit = False로 두고 인스턴스만 먼저 받은 후 requset 정보를 까서 clietn의 ip를 DB에 추가한다.)
    sales = models.IntegerField(validators=[numCheck])
    def get_absolute_url(self):
        return reverse('book:list')


