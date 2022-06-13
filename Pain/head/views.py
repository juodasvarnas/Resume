from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Вы находитесь на главной странице, это значит,что джанго работает!</h1>')

def test(request):
    return HttpResponse('Тестовая страница')

def head(request):
    return HttpResponse('<h1>Вы находитесь на главной странице приложения Head</h1>')
