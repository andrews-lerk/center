# Generated by Django 4.0.3 on 2022-04-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_osteopatdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_1', models.ImageField(upload_to='day_photos')),
                ('photo_2', models.ImageField(upload_to='day_photos')),
                ('photo_3', models.ImageField(upload_to='day_photos')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Описание дня здоровья',
                'verbose_name_plural': 'Описание дня здоровья',
            },
        ),
    ]
