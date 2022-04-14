from django.db import models
from main_app.models import Rooms


class Order(models.Model):
    check_in = models.DateField('Дата заезда')
    check_out = models.DateField('Дата выезда')
    room_type = models.CharField('Выбранный тип номера', max_length=10)
    room = models.ForeignKey(Rooms, verbose_name='Назначенный системой номер', on_delete=models.CASCADE)
    clients_info = models.TextField('Информация о пациентах')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    price = models.IntegerField(verbose_name='Итоговая стоимость курса (в рублях)')

    class Meta:
        verbose_name = 'Заявка для полного курса лечения'
        verbose_name_plural = 'Заявки для полного курса лечения'

    def __str__(self):
        return f'Заявка для номера: {self.phone}'
