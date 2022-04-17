from django.db import models
from main_app.models import Rooms


class Order(models.Model):
    STATUS = (('1', 'Оплачено',),
              ('2', 'Ожидает звонка администратора',),
              ('3', 'Процесс оплаты',),
              ('4', 'Отказано',),
              )

    check_in = models.DateField('Дата заезда')
    check_out = models.DateField('Дата выезда')
    room_type = models.CharField('Выбранный тип номера', max_length=10)
    room = models.ForeignKey(Rooms, verbose_name='Назначенный системой номер', on_delete=models.CASCADE)
    clients_info = models.TextField('Информация о пациентах')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    price = models.IntegerField(verbose_name='Итоговая стоимость курса (в рублях)')
    status = models.CharField('Статус', choices=STATUS, max_length=40, default='2')
    date_in_process_pay = models.DateField('Дата перевода в процесс оплаты', blank=True, null=True)
    pay_day = models.DateField('Дата оплаты', blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка для полного курса лечения'
        verbose_name_plural = 'Заявки для полного курса лечения'

    def __str__(self):
        return f'Заявка для номера: {self.phone}'


class OrderOsteopat(models.Model):
    STATUS = (('1', 'Оплачено',),
              ('2', 'Ожидает звонка администратора',),
              ('3', 'Процесс оплаты',),
              ('4', 'Отказано',),
              )

    check_in = models.DateField('Дата приема')
    clients_info = models.TextField('Информация о пациенте')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    price = models.IntegerField(verbose_name='Итоговая стоимость приема (в рублях)')
    status = models.CharField('Статус', choices=STATUS, default='2', max_length=40)
    date_in_process_pay = models.DateField('Дата перевода в процесс оплаты', blank=True, null=True)
    pay_day = models.DateField('Дата оплаты', blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка для приема остеопата'
        verbose_name_plural = 'Заявки для приема остеопата'

    def __str__(self):
        return f'Заявка для номера: {self.phone}'


class OrderDay(models.Model):
    STATUS = (('1', 'Оплачено',),
              ('2', 'Ожидает звонка администратора',),
              ('3', 'Процесс оплаты',),
              ('4', 'Отказано',),
              )

    check_in = models.DateField('Дата приема')
    clients_info = models.TextField('Информация о пациенте')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    price = models.IntegerField(verbose_name='Итоговая стоимость приема (в рублях)')
    status = models.CharField('Статус', choices=STATUS, default='2', max_length=40)
    date_in_process_pay = models.DateField('Дата перевода в процесс оплаты', blank=True, null=True)
    pay_day = models.DateField('Дата оплаты', blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка для дня здоровья'
        verbose_name_plural = 'Заявки для дня здоровья'

    def __str__(self):
        return f'Заявка для номера: {self.phone}'
