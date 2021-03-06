# Generated by Django 4.0.3 on 2022-04-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_prices_alter_dates_check_in_alter_dates_check_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='health_day',
            field=models.IntegerField(default=6800, verbose_name='День здоровья'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='luxe_room_full_health',
            field=models.IntegerField(default=9300, verbose_name='Сутки полного курса лечения (номер "комфорт")'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='osteopat',
            field=models.IntegerField(default=5000, verbose_name='Посещение остеопата'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='standart_room_full_health',
            field=models.IntegerField(default=8800, verbose_name='Сутки полного курса лечения (номер "стандарт")'),
        ),
    ]
