from django.urls import reverse, path
from django.utils.html import mark_safe
from django.contrib import admin
from .models import *
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ImageInline(admin.TabularInline):
    model = TourismImage


class ImageSmiInline(admin.TabularInline):
    model = SmiImage


class DescriptionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Description
        fields = '__all__'


class OfferAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Offer
        fields = '__all__'


class RulesAdminForm(forms.ModelForm):
    rules = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Rules
        fields = '__all__'


class MainCourseMiniAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = MainCourseMini
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


class DescriptionDayMiniAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = DayMiniDescription
        fields = '__all__'


class DescriptionOsteopatAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = OsteopatDescription
        fields = '__all__'


class DescriptionHealthBackAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HealthBack
        fields = '__all__'


class DescriptionHealthTourism3AdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HealthTourism3
        fields = '__all__'


class DescriptionHealthTourism5AdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HealthTourism5
        fields = '__all__'


class DescriptionHealthTourism7AdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HealthTourism7
        fields = '__all__'


class DescriptionHealthTourism10AdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HealthTourism10
        fields = '__all__'


class DescriptionTourismAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Tourism
        fields = '__all__'


class DescriptionSmiAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Smi
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


@admin.register(HealthBack)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionHealthBackAdminForm


@admin.register(HealthTourism3)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionHealthTourism3AdminForm


@admin.register(HealthTourism5)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionHealthTourism5AdminForm


@admin.register(HealthTourism7)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionHealthTourism7AdminForm


@admin.register(HealthTourism10)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionHealthTourism10AdminForm


@admin.register(MainCourse)
class MainCourseAdmin(admin.ModelAdmin):
    form = DescriptionMainCourseAdminForm


@admin.register(Tourism)
class TourismAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    form = DescriptionTourismAdminForm


@admin.register(Smi)
class TourismAdmin(admin.ModelAdmin):
    inlines = [ImageSmiInline, ]
    form = DescriptionSmiAdminForm


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(OsteopatDescription)
class CategoriesAdmin(admin.ModelAdmin):
    form = DescriptionOsteopatAdminForm


@admin.register(DayDescription)
class CategoriesAdmin(admin.ModelAdmin):
    form = DescriptionDayAdminForm


@admin.register(DayMiniDescription)
class DayMiniAdmin(admin.ModelAdmin):
    form = DescriptionDayMiniAdminForm


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    form = RulesAdminForm


@admin.register(MainCourseMini)
class MainCourseMiniAdmin(admin.ModelAdmin):
    form = MainCourseMiniAdminForm


@admin.register(Offer)
class MainCourseMiniAdmin(admin.ModelAdmin):
    form = OfferAdminForm


admin.site.register(MainPhotos)
admin.site.register(GalleryCategory)
admin.site.register(Gallery)
admin.site.register(MainPhone)
admin.site.register(Staff)
admin.site.register(NumberImages)
admin.site.register(CoursesPhoto)
admin.site.register(Prices)
admin.site.register(Procedures)
