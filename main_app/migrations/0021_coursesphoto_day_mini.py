# Generated by Django 4.0.3 on 2023-01-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_dayminidescription_prices_health_day_mini'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesphoto',
            name='day_mini',
            field=models.ImageField(null=True, upload_to='course_photos'),
        ),
    ]
