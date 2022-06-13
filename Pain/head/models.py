from dataclasses import asdict
from urllib.request import AbstractDigestAuthHandler
from django.db import models

# Create your models here.


class Pain(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Имя, Фамилия, Отчество')
    prof_skills = models.TextField(verbose_name='Профессиональные навыки')
    social_skills = models.TextField(verbose_name='Социальные навыки')
    start_work = models.DateField(auto_now=False, verbose_name='Принят на работу')
    end_work = models.DateField(auto_now=False, verbose_name='Окончание работы')
    photo = models.ImageField(upload_to='images/%y/%m/%d/', verbose_name='Фото', blank=True)
    job_title = models.CharField(max_length=150, verbose_name='Должность')
    duty = models.TextField(verbose_name='Обязанности')
    Now_job = models.CharField(max_length=150, verbose_name='Желаемая должность')
    money = models.IntegerField(verbose_name='Уровень ЗП')
    contacts = models.TextField(verbose_name='Мои контакты')
    #experience = models.ForeignKey('Experience', on_delete=models.PROTECT, verbose_name='Опыт работы')

