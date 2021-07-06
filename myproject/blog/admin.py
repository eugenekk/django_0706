from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

# Register your models here.

# admin 페이지에서 Post 테이블 관리할 수 있게 등록

# 방법1) admin 제공 그대로 사용
# admin.site.register(Post) -> 아래 커스텀에서 사용
# admin.site.register(Comment)
admin.site.register(Tag)

# 방법2) 커스텀 하기
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','content_size2','created_at','updated_at'] # admin에서 보이는 컬럼 이름들
    list_display_links = ['id', 'title']
    fields = ['title','content','user']
    list_filter = ['created_at']
    search_fields = ['title']
    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    def content_size2(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))

    content_size.short_description = '글자수'
    content_size2.short_description = '글자수2'


admin.site.register(Post, PostAdmin)

# 방법3) 커스텀 하기2
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post','author','message', 'created_at', 'updated_at']