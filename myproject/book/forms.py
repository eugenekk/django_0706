from django import forms
from django.db.models import fields
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.Form):
    title = forms.CharField(label="제목")
    author = forms.CharField(label="저자")
    publisher = forms.CharField(label="출판사", required=False)

    # DB 입력(추가)방법 3 : Form 내부에 save 메소드 생성(추가된 기능 commit)
    def save(self, commit=False):
        book = Book(**self.cleaned_data)
        if commit:
            book.save()
        return book


# form생성방법 3 : Model을 기반으로 form 자동생성
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = '__all__'  # 컬럼 전체 form 생성
        fields = ['title', 'author', 'publisher', 'sales']

    def clean_author(self):
        author = self.cleaned_data.get('author', '').strip()
        if author:
            if len(author) < 3:
                raise ValidationError('최소 3글자 이상 입력하세요')
        return author
    
    def clean(self):
        cleaned_data = super().clean()
        if self.check_exist(cleaned_data.get('title'), cleaned_data.get('author')):
            raise ValidationError('이미 등록된 책입니다.')
        return cleaned_data

    def check_exist(self, title, author):
        return Book.objects.filter(title =title, author=author)
