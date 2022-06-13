from django.urls import path,include
from .views import *

urlpatterns = [
    path('', head),
    path('test/', test),
]
