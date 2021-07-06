from django.http import response
from django.http.response import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Post
import os
from django.conf import settings

# Create your views here.
# blog App 에서 구현할 서비스를 작성합니다.

def index(request):
    post_list = Post.objects.all()
    output = ','.join([p.title for p in post_list])
    return HttpResponse(output)

def index2(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':post_list})

# def detail(request, id): #urls.py 에서 인자로 받기로 한 url정보
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("page not found")
#     return render(request, 'blog/detail.html', {'post':post})

def detail(request, id): #urls.py 에서 인자로 받기로 한 url정보
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post':post})

def json_test(request):
    music = {'singer':'BTS', 'songs': ['Fake Love', 'DNA', '피땀눈물', '봄날']}
    return JsonResponse(music, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'demo.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response["Content-Disposition"] = "attachment; filename={}".format(filename)
        return response

def get_redirect1(request):
    return redirect('/blog/', permanent=True) 

def get_redirect2(request):
    return redirect('http://google.com')

def test2(request, id):
    print(type(id))
    return HttpResponse(id)

# 120p Variables 템플릿 태그 테스트 위한 복붙
from django.utils import timezone

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return 'hello'
        
def test4(request):
    people = ['Amy', 'Josh', 'Tobey', 'John']
    person = Person('Amy')
    person_list = []
    now = timezone.now()
    past_dt = timezone.datetime(1971,8,22,0,0)
    criteria_dt = timezone.datetime(2001,3,19,0,0)
    future_dt = timezone.datetime(2037,1,1,0,0)

    msg = '''
        Miracles happen to only those who believe in them.
        Think like a man of action and act like man of thought.
        Courage is very important. Like a muscle, it is strengthened by use.
        Life is the art of drawing sufficient conclusions from insufficient premises.
        By doubting we come at the truth.
        A man that has no virtue in himself, ever envies virtue in others.
        When money speaks, the truth keeps silent.
        Better the last smile than the first laughter.
    '''


    value = '<b>Joel</b> <button>is</button> a <span>slug</span>'
    value1 = 'Joel is a slug'
    value2 = '<p>Joel is a slug</p>'
    value3 = "https://www.example.org/foo?a=b&c=d"
    value4 = "Check out www.djangoproject.com"
    value5 = "Send questions to foo@example.com"

    return render(request, 'test.html', {'people':people, 'person':person, 'person_list':person_list, 
                                                'datetime_obj':now, 'past_dt':past_dt, 'criteria_dt':criteria_dt, 
                                                'future_dt':future_dt, 'value':value, 'value1':value1,
                                                'value2':value2, 'value3':value3, 'value4':value4,
                                                'value5':value5, 'msg':msg})

# Model로 form 만들기
# http://localhost:8000/blog/test5/ : 같은 url에서 두가지 요청을 GET/POST 나눠서
def test5(request):
    if request.method =='POST':
        pass
    else:
        return render(request, 'member.html')
