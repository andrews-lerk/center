from django.http import HttpResponseRedirect
from django.contrib import admin
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

