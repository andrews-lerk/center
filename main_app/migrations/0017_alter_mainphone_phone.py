# Generated by Django 4.0.3 on 2022-04-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_mainphone_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainphone',
            name='phone',
            field=models.CharField(max_length=19, verbose_name='Телефон на главной'),
        ),
    ]
