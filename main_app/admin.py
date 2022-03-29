from django.urls import reverse, path
from django.utils.html import mark_safe
from django.contrib import admin
from .models import *
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DescriptionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Description
        fields = '__all__'


class DescriptionMainCourseAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = MainCourse
        fields = '__all__'


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('edit', 'active',)
    form = DescriptionAdminForm

    @admin.display(description='')
    def edit(self, obj):
        url = reverse('admin:main_app_description_change', args=(obj.id,))
        return mark_safe(f'<a class="button" href="{url}">Просмотреть\редактировать</a>')


@admin.register(Dates)
class DatesAdmin(admin.ModelAdmin):
    list_display = ('period', 'room')

    @admin.display(description='Период')
    def period(self, obj):
        period = f'{obj.check_in.strftime("%d/%m/%Y")} - {obj.check_out.strftime("%d/%m/%Y")}'
        return period


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_type',)


@admin.register(MainCourse)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionMainCourseAdminForm


admin.site.register(MainPhotos)
admin.site.register(CoursesPhoto)
admin.site.register(Order)
