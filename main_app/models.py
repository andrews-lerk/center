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
    full_course_maxi = models.ImageField(upload_to='course_photos')
    full_course_mini = models.ImageField(upload_to='course_photos', null=True)
    day = models.ImageField(upload_to='course_photos')
    day_mini = models.ImageField(upload_to='course_photos', null=True)
    osteopat = models.ImageField(upload_to='course_photos')

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
        verbose_name = 'Описание полного курса МАКСИ'
        verbose_name_plural = 'Описание для полного курса МАКСИ'

    def __str__(self):
        return 'Описание для полного курса МАКСИ'


class MainCourseMini(models.Model):
    photo_1 = models.ImageField(upload_to='main_course_photos')
    photo_2 = models.ImageField(upload_to='main_course_photos')
    photo_3 = models.ImageField(upload_to='main_course_photos')
    description = models.TextField()

    class Meta:
        verbose_name = 'Описание полного курса МИНИ'
        verbose_name_plural = 'Описание для полного курса МИНИ'

    def __str__(self):
        return 'Описание для полного курса МИНИ'


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


class DayMiniDescription(models.Model):
    photo_1 = models.ImageField(upload_to='day_photos')
    photo_2 = models.ImageField(upload_to='day_photos')
    photo_3 = models.ImageField(upload_to='day_photos')
    description = models.TextField()

    class Meta:
        verbose_name = 'Описание дня здоровья мини'
        verbose_name_plural = 'Описание дня здоровья мини'

    def __str__(self):
        return 'Описание дня здоровья мини'


class Prices(models.Model):
    full_health_maxi = models.IntegerField(verbose_name='Сутки полного курса лечения МАКСИ',
                                                    default=8800)
    full_health_mini = models.IntegerField(verbose_name='Сутки полного курса лечения МИНИ',
                                                    default=8800)
    health_day = models.IntegerField(verbose_name='День здоровья', default=6800)
    health_day_mini = models.IntegerField(verbose_name='День здоровья "мини"', default=2700)
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


class GalleryCategory(models.Model):
    category = models.CharField('Категория', max_length=255)

    class Meta:
        verbose_name = 'Категория для галерии'
        verbose_name_plural = 'Категории для галерии'

    def __str__(self):
        return self.category


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.image.url


class MainPhone(models.Model):
    phone = models.CharField('Телефон на главной', max_length=19)

    class Meta:
        verbose_name = 'Телефон на главной'
        verbose_name_plural = 'Телефон на главной'

    def __str__(self):
        return self.phone


class Staff(models.Model):
    name = models.CharField('Имя и фамилия', max_length=255)
    image = models.ImageField('Фото', upload_to='staff')
    level = models.CharField('Должность', max_length=255)

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return self.name


class NumberImages(models.Model):
    luxe = models.ImageField('Комфорт', upload_to='numbers')
    standart = models.ImageField('Стандарт', upload_to='numbers')

    class Meta:
        verbose_name = 'Фото комнат'
        verbose_name_plural = 'Фото комнат'

    def __str__(self):
        return 'Фото комнат'


class Rules(models.Model):
    rules = models.TextField('Правила')

    class Meta:
        verbose_name = 'Правила посещения'
        verbose_name_plural = 'Правила посещения'

    def __str__(self):
        return 'Правила посещения'
