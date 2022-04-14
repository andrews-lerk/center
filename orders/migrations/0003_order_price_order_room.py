# Generated by Django 4.0.3 on 2022-04-14 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_delete_dates'),
        ('orders', '0002_alter_order_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.rooms', verbose_name='Назначенный системой номер'),
            preserve_default=False,
        ),
    ]
