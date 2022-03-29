from django.db import models


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


class Dates(models.Model):
    check_in = models.DateField('Дата заезда')
    check_out = models.DateField('Дата выезда')
    room = models.OneToOneField('Rooms', related_name='room_date', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Занятая дата'
        verbose_name_plural = 'Занятые даты'


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
        return self.title


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


class Order(models.Model):
    check_in = models.DateField('Дата заезда')
    check_out = models.DateField('Дата выезда')
    room_type = models.CharField('Выбранный тип номера', max_length=10)
    clients_info = models.TextField('Информация о пациентах')
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка для номера: {self.phone}'
