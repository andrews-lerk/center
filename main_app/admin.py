from django.http import HttpResponseRedirect
from django.urls import reverse, path
from django.utils.html import mark_safe
from django.contrib import admin
from .models import *
from django import forms
from django.contrib import messages
from .utils import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ImageInline(admin.TabularInline):
    model = TourismImage


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


class DescriptionDayAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = DayDescription
        fields = '__all__'


class DescriptionOsteopatAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = OsteopatDescription
        fields = '__all__'


class DescriptionTourismAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Tourism
        fields = '__all__'


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('edit', 'active',)
    form = DescriptionAdminForm

    @admin.display(description='')
    def edit(self, obj):
        url = reverse('admin:main_app_description_change', args=(obj.id,))
        return mark_safe(f'<a class="button" href="{url}">Просмотреть\редактировать</a>')


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('full_title', 'room_type',)

    @admin.display(description='Название')
    def full_title(self, obj):
        return f'{obj.title} {obj.pk}'


@admin.register(MainCourse)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionMainCourseAdminForm


@admin.register(Tourism)
class TourismAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    form = DescriptionTourismAdminForm


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(OsteopatDescription)
class CategoriesAdmin(admin.ModelAdmin):
    form = DescriptionOsteopatAdminForm


@admin.register(DayDescription)
class CategoriesAdmin(admin.ModelAdmin):
    form = DescriptionDayAdminForm


admin.site.register(MainPhotos)
admin.site.register(GalleryCategory)
admin.site.register(Gallery)
admin.site.register(MainPhone)
admin.site.register(Staff)
admin.site.register(CoursesPhoto)
admin.site.register(Prices)
