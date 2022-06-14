from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Pain


def index(request):
    pain = Pain.objects.all()
    
    return render(request, 'head/index.html',{'pain':pain, 'Name':'имя пользователя'})

def test(request):
    return HttpResponse('Тестовая страница')

def head(request):
    return HttpResponse('<h1>Вы находитесь на главной странице приложения Head</h1>')
