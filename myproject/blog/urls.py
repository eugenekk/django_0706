from re import VERBOSE
from django.urls import path, include, register_converter
from . import views
from .converters import CodeConverter

register_converter(CodeConverter, 'dddd')

urlpatterns = [
    path('test3/', views.get_redirect2),
    path('file/', views.excel_download),
    path('json/', views.json_test),
    path('detail/<id>/', views.detail),
    path('', views.index2),
    path('test/', views.index),
    path('test2/<dddd:id>', views.test2), # id라는 인자를 받아서 씀
    path('test4/', views.test4),
    path('test5/', views.test5),
]
