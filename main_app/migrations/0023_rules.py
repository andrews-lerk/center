# Generated by Django 4.0.3 on 2023-03-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_rename_left_coursesphoto_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.TextField(verbose_name='Правила')),
            ],
            options={
                'verbose_name': 'Правила посещения',
                'verbose_name_plural': 'Правила посещения',
            },
        ),
    ]