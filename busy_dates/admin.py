from django.http import HttpResponseRedirect
from django.contrib import admin
from main_app.utils import get_busy_rooms
from .models import *
from django.urls import reverse, path


@admin.register(Dates)
class DatesAdmin(admin.ModelAdmin):
    list_display = ('date_or_period', 'course_type', 'room')

    @admin.display(description='Период')
    def date_or_period(self, obj):
        if obj.course_type == '1':
            date_or_period = f'{obj.check_in.strftime("%d/%m/%Y")} - {obj.check_out.strftime("%d/%m/%Y")}'
        else:
            date_or_period = f'{obj.course_date.strftime("%d/%m/%Y")}'
        return date_or_period

    def response_add(self, request, obj, post_url_continue=None):
        url = reverse('admin:busy_dates_dates_changelist')
        return HttpResponseRedirect(url)

    def response_change(self, request, obj):
        url = reverse('admin:busy_dates_dates_changelist')
        return HttpResponseRedirect(url)

    def save_model(self, request, obj, form, change):
        if obj.course_type == "1":
            if obj.course_date is not None or obj.check_in is None or obj.check_out is None or obj.room is None:
                return messages.error(request, 'Дата не была добавлена, так как для выбранного типа лечения вы '
                                               'указали некорректные данные, пожалуйста '
                                               'введите данные правильно!')

            if obj.check_in >= obj.check_out:
                return messages.error(request, 'Дата заезда не может быть позже даты выезда!')

            if obj.room.id in get_busy_rooms(check_in_client=obj.check_in, checkout_out_client=obj.check_out)[
                'luxe_busy_id'] or obj.room.id in \
                    get_busy_rooms(check_in_client=obj.check_in, checkout_out_client=obj.check_out)[
                        'standart_busy_id']:
                return messages.error(request, 'Дата с выбранной вами комнатой уже занята!')

            else:
                messages.success(request, "Дата успешно добавлена!")
                super().save_model(request, obj, form, change)

        else:
            if obj.course_date is None or obj.check_in is not None or obj.check_out is not None or obj.room is not None:
                return messages.error(request, 'Дата не была добавлена, так как для выбранного типа лечения вы '
                                               'указали некорректные данные, пожалуйста '
                                               'введите данные правильно!')
            else:
                messages.success(request, "Дата успешно добавлена!")
                super().save_model(request, obj, form, change)
