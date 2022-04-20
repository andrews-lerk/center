from django.contrib import admin
from .models import *
from django.shortcuts import redirect
from django.urls import path, include
from django.urls import reverse
from django.utils.html import mark_safe
from datetime import date


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('for_', 'paid', 'deny', 'process', 'status_',)

    @admin.display(description='Заявка для')
    def for_(self, obj):
        return f'Заявка для номера: {obj.phone}'

    @admin.display(description='Статус')
    def status_(self, obj):
        if obj.status == '4':
            return mark_safe(f'<p style="color: red">Отказано</p>')
        if obj.status == '3':
            return mark_safe(f'<p style="color: orange">Процесс оплаты клиента</p>')
        if obj.status == '2':
            return mark_safe(f'<p style="color: navy">Ожидает звонка администратора</p>')
        if obj.status == '1':
            return mark_safe(f'<p style="color: green">Оплачено</p>')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/paid/', self.do_paid, name='paid'),
            path('<int:pk>/deny/', self.do_deny, name='deny'),
            path('<int:pk>/process-pay/', self.do_process, name='process'),
        ]
        return custom_urls + urls

    @admin.display(description='Оплачено')
    def paid(self, obj):
        url = reverse('admin:paid', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Оплачено</a>')

    @admin.display()
    def do_paid(self, obj, pk):
        order = Order.objects.get(pk=pk)
        order.status='1'
        order.pay_day = date.today()
        order.save()
        redirect_url = reverse('admin:orders_order_changelist')
        return redirect(redirect_url)

    @admin.display(description='Отказать')
    def deny(self, obj):
        url = reverse('admin:deny', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Отказать</a>')

    @admin.display()
    def do_deny(self, obj, pk):
        order = Order.objects.get(pk=pk)
        order.status = '4'
        order.save()
        redirect_url = reverse('admin:orders_order_changelist')
        return redirect(redirect_url)

    @admin.display(description='Процесс оплаты')
    def process(self, obj):
        url = reverse('admin:process', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Процесс оплаты</a>')

    @admin.display()
    def do_process(self, obj, pk):
        order = Order.objects.get(pk=pk)
        order.status = '3'
        order.date_in_process_pay = date.today()
        order.save()
        redirect_url = reverse('admin:orders_order_changelist')
        return redirect(redirect_url)

@admin.register(OrderOsteopat)
class OrderOsteopatAdmin(admin.ModelAdmin):
    list_display = ('for_', 'paid', 'deny', 'process', 'status_',)

    @admin.display(description='Заявка для')
    def for_(self, obj):
        return f'Заявка для номера: {obj.phone}'

    @admin.display(description='Статус')
    def status_(self, obj):
        if obj.status == '4':
            return mark_safe(f'<p style="color: red">Отказано</p>')
        if obj.status == '3':
            return mark_safe(f'<p style="color: orange">Процесс оплаты клиента</p>')
        if obj.status == '2':
            return mark_safe(f'<p style="color: navy">Ожидает звонка администратора</p>')
        if obj.status == '1':
            return mark_safe(f'<p style="color: green">Оплачено</p>')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/paid-osteopat/', self.do_paid, name='paid-osteopat'),
            path('<int:pk>/deny-osteopat/', self.do_deny, name='deny-osteopat'),
            path('<int:pk>/process-osteopat/', self.do_process, name='process-osteopat'),
        ]
        return custom_urls + urls

    @admin.display(description='Оплачено')
    def paid(self, obj):
        url = reverse('admin:paid-osteopat', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Оплачено</a>')

    @admin.display()
    def do_paid(self, obj, pk):
        order = OrderOsteopat.objects.get(pk=pk)
        order.status = '1'
        order.pay_day = date.today()
        order.save()
        redirect_url = reverse('admin:orders_orderosteopat_changelist')
        return redirect(redirect_url)

    @admin.display(description='Отказать')
    def deny(self, obj):
        url = reverse('admin:deny-osteopat', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Отказать</a>')

    @admin.display()
    def do_deny(self, obj, pk):
        order = OrderOsteopat.objects.get(pk=pk)
        order.status = '4'
        order.save()
        redirect_url = reverse('admin:orders_orderosteopat_changelist')
        return redirect(redirect_url)

    @admin.display(description='Процесс оплаты')
    def process(self, obj):
        url = reverse('admin:process-osteopat', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Процесс оплаты</a>')

    @admin.display()
    def do_process(self, obj, pk):
        order = OrderOsteopat.objects.get(pk=pk)
        order.status = '3'
        order.date_in_process_pay = date.today()
        order.save()
        redirect_url = reverse('admin:orders_orderosteopat_changelist')
        return redirect(redirect_url)

@admin.register(OrderDay)
class OrderDayAdmin(admin.ModelAdmin):
    list_display = ('for_', 'paid', 'deny', 'process', 'status_',)

    @admin.display(description='Заявка для')
    def for_(self, obj):
        return f'Заявка для номера: {obj.phone}'

    @admin.display(description='Статус')
    def status_(self, obj):
        if obj.status == '4':
            return mark_safe(f'<p style="color: red">Отказано</p>')
        if obj.status == '3':
            return mark_safe(f'<p style="color: orange">Процесс оплаты клиента</p>')
        if obj.status == '2':
            return mark_safe(f'<p style="color: navy">Ожидает звонка администратора</p>')
        if obj.status == '1':
            return mark_safe(f'<p style="color: green">Оплачено</p>')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/paid-day/', self.do_paid, name='paid-day'),
            path('<int:pk>/deny-day/', self.do_deny, name='deny-day'),
            path('<int:pk>/process-day/', self.do_process, name='process-day'),
        ]
        return custom_urls + urls

    @admin.display(description='Оплачено')
    def paid(self, obj):
        url = reverse('admin:paid-day', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Оплачено</a>')

    @admin.display()
    def do_paid(self, obj, pk):
        order = OrderDay.objects.get(pk=pk)
        order.status = '1'
        order.pay_day = date.today()
        order.save()
        redirect_url = reverse('admin:orders_orderday_changelist')
        return redirect(redirect_url)

    @admin.display(description='Отказать')
    def deny(self, obj):
        url = reverse('admin:deny-day', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Отказать</a>')

    @admin.display()
    def do_deny(self, obj, pk):
        order = OrderDay.objects.get(pk=pk)
        order.status = '4'
        order.save()
        redirect_url = reverse('admin:orders_orderday_changelist')
        return redirect(redirect_url)

    @admin.display(description='Процесс оплаты')
    def process(self, obj):
        url = reverse('admin:process-day', args=[obj.pk])
        return mark_safe(f'<a class="button" href="{url}">Процесс оплаты</a>')

    @admin.display()
    def do_process(self, obj, pk):
        order = OrderDay.objects.get(pk=pk)
        order.status = '3'
        order.date_in_process_pay = date.today()
        order.save()
        redirect_url = reverse('admin:orders_orderday_changelist')
        return redirect(redirect_url)
