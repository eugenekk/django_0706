from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from .models import Book
from .forms import BookForm, BookModelForm
from django.http import HttpResponse
# Create your views here.

# book_new = CreateView.as_view(model=Book, fielss='__all__')

def book_new(request):
    if request.method == 'POST':
        # form = BookForm(request.POST) # 데이터 바인딩(form 수동생성사용)
        form = BookModelForm(request.POST) # 데이터 바인딩(ModelForm 사용)
        if form.is_valid():
            print(form.cleaned_data);
            # DB 입력(추가)방법 1
            # book = Book(**form.cleaned_data) # **데이터언패킹
            # book.save()

            # DB 입력(추가)방법 2
            # book = Book.objects.create(**form.cleaned_data)

            # DB 입력(추가)방법 3
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
            book.save()

            return redirect(book)
    else:
        # form = BookForm()
        form = BookModelForm() #(ModelForm 사용)
    return render(request, 'book/book_form.html', {'form':form})

def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'book/book_list.html', {'book_list':book_list})

def book_edit(request, id):
    book = get_object_or_404(Book, id=id) #요청한 id에 해당하는 인스턴스 가져오기(기존데이터)

    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
            book.save()
            print(book)
            return redirect(book)

    else: # GET 방식으로 들어올 경우 채워진 입력폼 제공
        form = BookModelForm(instance = book)
        return render(request, 'book/book_form.html', {'form':form})
