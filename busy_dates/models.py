from django.db import models
from main_app.models import *
from django.contrib import messages


class Dates(models.Model):
    TYPES = (
        ('1', 'Полный курс лечения',),
        ('2', 'День здоровья',),
        ('3', 'Посещение остеопата',)
    )
    course_type = models.CharField(verbose_name='Тип лечения',
                                   choices=TYPES, max_length=1, default='1', null=True, blank=True)
    course_date = models.DateField(verbose_name='День лечения ',
                                   help_text='Только для дня здоровья или остеопата', null=True, blank=True)
    check_in = models.DateField(verbose_name='Дата заезда',
                                help_text='Только для полного курса лечения', null=True, blank=True)
    check_out = models.DateField(verbose_name='Дата выезда',
                                 help_text='Только для полного курса лечения', null=True, blank=True)
    room = models.ForeignKey(Rooms, verbose_name='Тип комнаты', related_name='room_date',
                             help_text='Только для полного курса лечения',
                             on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Занятая дата'
        verbose_name_plural = 'Занятые даты'
