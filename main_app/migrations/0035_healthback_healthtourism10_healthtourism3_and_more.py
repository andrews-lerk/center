# Generated by Django 4.0.3 on 2023-10-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_alter_smi_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_1', models.ImageField(upload_to='main_course_photos')),
                ('photo_2', models.ImageField(upload_to='main_course_photos')),
                ('photo_3', models.ImageField(upload_to='main_course_photos')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Описание для здоровой спины',
                'verbose_name_plural': 'Описание для здоровой спины',
            },
        ),
        migrations.CreateModel(
            name='HealthTourism10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_1', models.ImageField(upload_to='main_course_photos')),
                ('photo_2', models.ImageField(upload_to='main_course_photos')),
                ('photo_3', models.ImageField(upload_to='main_course_photos')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Описание для лечения и туризма 10 дней',
                'verbose_name_plural': 'Описание для лечения и туризма 10 дней',
            },
        ),
        migrations.CreateModel(
            name='HealthTourism3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_1', models.ImageField(upload_to='main_course_photos')),
                ('photo_2', models.ImageField(upload_to='main_course_photos')),
                ('photo_3', models.ImageField(upload_to='main_course_photos')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Описание для лечения и туризма 3 дня',
                'verbose_name_plural': 'Описание для лечения и туризма 3 дня',
            },
        ),
        migrations.CreateModel(
            name='HealthTourism5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_1', models.ImageField(upload_to='main_course_photos')),
                ('photo_2', models.ImageField(upload_to='main_course_photos')),
                ('photo_3', models.ImageField(upload_to='main_course_photos')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Описание для лечения и туризма 5 дня',
                'verbose_name_plural': 'Описание для лечения и туризма 5 дня',
            },
        ),
        migrations.CreateModel(
            name='HealthTourism7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_1', models.ImageField(upload_to='main_course_photos')),
                ('photo_2', models.ImageField(upload_to='main_course_photos')),
                ('photo_3', models.ImageField(upload_to='main_course_photos')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to='main_course_photos')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Описание для лечения и туризма 7 дней',
                'verbose_name_plural': 'Описание для лечения и туризма 7 дней',
            },
        ),
        migrations.AddField(
            model_name='coursesphoto',
            name='health_back',
            field=models.ImageField(blank=True, null=True, upload_to='course_photos'),
        ),
        migrations.AddField(
            model_name='coursesphoto',
            name='health_tourism_10',
            field=models.ImageField(blank=True, null=True, upload_to='course_photos'),
        ),
        migrations.AddField(
            model_name='coursesphoto',
            name='health_tourism_3',
            field=models.ImageField(blank=True, null=True, upload_to='course_photos'),
        ),
        migrations.AddField(
            model_name='coursesphoto',
            name='health_tourism_5',
            field=models.ImageField(blank=True, null=True, upload_to='course_photos'),
        ),
        migrations.AddField(
            model_name='coursesphoto',
            name='health_tourism_7',
            field=models.ImageField(blank=True, null=True, upload_to='course_photos'),
        ),
        migrations.AddField(
            model_name='prices',
            name='health_back',
            field=models.IntegerField(default=8800, verbose_name='Здоровая спина'),
        ),
        migrations.AddField(
            model_name='prices',
            name='health_tourism_10',
            field=models.IntegerField(default=8800, verbose_name='Здоровье и туризм 10 дня'),
        ),
        migrations.AddField(
            model_name='prices',
            name='health_tourism_3',
            field=models.IntegerField(default=8800, verbose_name='Здоровье и туризм 3 дня'),
        ),
        migrations.AddField(
            model_name='prices',
            name='health_tourism_5',
            field=models.IntegerField(default=8800, verbose_name='Здоровье и туризм 5 дня'),
        ),
        migrations.AddField(
            model_name='prices',
            name='health_tourism_7',
            field=models.IntegerField(default=8800, verbose_name='Здоровье и туризм 7 дня'),
        ),
    ]
