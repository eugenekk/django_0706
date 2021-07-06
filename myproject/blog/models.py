from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    REGION_CHOICE = (
        ('Africa', '아프리카'),
        ('Europe', '유럽'),
        ('Oceania', '오세아니아'),
        ('Asia', '아시아'),
        ('North America', '북아메리카'),
        ('South America', '남아메리카'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name="제목", help_text="제목을 입력해주세요. 최대 100자")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
    inglat = models.CharField(max_length=50, blank=True, help_text="경도, 위도 포맷으로 입력")
    region = models.CharField(max_length=20, choices=REGION_CHOICE, default='Asia')
    # M:M 관계 Tag 필드 추가
    tag_set = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title  # __str__ 메소드 오버라이딩(p1안의 내용을 보고싶을 때)


# 1:N 관계 1(Post) : N(Comment)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message # __str__ 메소드 오버라이딩(p1안의 내용을 보고싶을 때)

# M:M 관계 M(Post) : M(Tag) : M:M은 둘중 하나에 컬럼 추가하면됨(Post에 tag_set 컬럼 추가)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name