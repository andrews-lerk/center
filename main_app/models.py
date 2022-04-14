from django.db import models
from django.shortcuts import redirect


class MainPhotos(models.Model):
    photo_1 = models.ImageField(upload_to='big_photos')
    photo_2 = models.ImageField(upload_to='big_photos')
    photo_3 = models.ImageField(upload_to='big_photos')

    class Meta:
        verbose_name = 'Главные фото'
        verbose_name_plural = 'Главные фото'

    def __str__(self):
        return 'Фото с главной страницы'


class CoursesPhoto(models.Model):
    right = models.ImageField(upload_to='course_photos')
    middle = models.ImageField(upload_to='course_photos')
    left = models.ImageField(upload_to='course_photos')

    class Meta:
        verbose_name = 'Фото курсов лечения на главной странице'
        verbose_name_plural = 'Фото курсов лечения на главной странице'

    def __str__(self):
        return 'Фото с курсов лечения на главной странице'


class Description(models.Model):
    description = models.TextField()
    active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Об Амбер Сакрум '
        verbose_name_plural = 'Об Амбер Сакрум'

    def __str__(self):
        return 'Описание на главной странице'


class Rooms(models.Model):
    TYPES = (
        ('1', 'Комфорт',),
        ('2', 'Стандарт',),
    )

    room_type = models.CharField('Тип номера', choices=TYPES, max_length=1, default='1')
    title = models.CharField('Название', max_length=63)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return f'{self.title} {self.id}'


class MainCourse(models.Model):
    photo_1 = models.ImageField(upload_to='main_course_photos')
    photo_2 = models.ImageField(upload_to='main_course_photos')
    photo_3 = models.ImageField(upload_to='main_course_photos')
    description = models.TextField()

    class Meta:
        verbose_name = 'Описание полного курса'
        verbose_name_plural = 'Описание для полного курса'

    def __str__(self):
        return 'Описание для полного курса'


class OsteopatDescription(models.Model):
    photo_1 = models.ImageField(upload_to='osteopat_photos')
    photo_2 = models.ImageField(upload_to='osteopat_photos')
    photo_3 = models.ImageField(upload_to='osteopat_photos')
    description = models.TextField()

    class Meta:
        verbose_name = 'Описание посещения остеопата'
        verbose_name_plural = 'Описание посещения остеопата'

    def __str__(self):
        return 'Описание для посещения остеопата'


class DayDescription(models.Model):
    photo_1 = models.ImageField(upload_to='day_photos')
    photo_2 = models.ImageField(upload_to='day_photos')
    photo_3 = models.ImageField(upload_to='day_photos')
    description = models.TextField()

    class Meta:
        verbose_name = 'Описание дня здоровья'
        verbose_name_plural = 'Описание дня здоровья'

    def __str__(self):
        return 'Описание дня здоровья'


class Prices(models.Model):
    luxe_room_full_health = models.IntegerField(verbose_name='Сутки полного курса лечения (номер "комфорт")',
                                                default=9300)
    standart_room_full_health = models.IntegerField(verbose_name='Сутки полного курса лечения (номер "стандарт")',
                                                    default=8800)
    health_day = models.IntegerField(verbose_name='День здоровья', default=6800)
    osteopat = models.IntegerField(verbose_name='Посещение остеопата', default=5000)

    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс лист'

    def __str__(self):
        return 'Изменить прайс лист для курсов лечения'


class Categories(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name = 'Категория для туризма и досуга'
        verbose_name_plural = 'Категории для туризма и досуга'


class Tourism(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Запись для досуга и туризма'
        verbose_name_plural = 'Записи для досуга и туризма'

    def get_images(self):
        return self.tourism_record.all()


class TourismImage(models.Model):
    image = models.ImageField(upload_to='tourism_and_dosug')
    record = models.ForeignKey(Tourism, on_delete=models.CASCADE, related_name='tourism_record')