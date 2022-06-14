from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Pain


def index(request):
    pain = Pain.objects.all()
    res = '<h1>На должность представляем</h1>'
    for item in pain:
         res+= f'<div>\n<p>{item.Name}</p>\n<p>{item.photo}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)

def test(request):
    return HttpResponse('Тестовая страница')

def head(request):
    return HttpResponse('<h1>Вы находитесь на главной странице приложения Head</h1>')
