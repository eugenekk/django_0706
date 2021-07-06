from django.contrib import admin
from .models import Article

# Register your models here.
def make_published(self, request, queryset):
    queryset.update(status = 'p')

make_published.short_description = '선택된 articles를 Published 상태로 변경합니다.'

def make_draft(self, request, queryset):
    queryset.update(status = 'd')

make_draft.short_description = '선택된 articles를 draft 상태로 변경합니다.'

def make_withdrawn(self, request, queryset):
    queryset.update(status = 'w')

make_withdrawn.short_description = '선택된 articles를 withdrawn 상태로 변경합니다.'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published, make_draft, make_withdrawn]

admin.site.register(Article, ArticleAdmin)
