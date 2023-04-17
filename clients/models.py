from django.db import models


class Clients(models.Model):
    phone = models.CharField('Номер телефона', max_length=20, unique=True)
    name = models.CharField('ФИО клиента', max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name + ' ; ' + self.phone
