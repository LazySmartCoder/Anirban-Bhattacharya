# Generated by Django 4.0.6 on 2022-08-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnirbanBhattacharyaWebsite', '0012_hired_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hired',
            name='Budget',
            field=models.IntegerField(default='', max_length=50),
        ),
    ]
