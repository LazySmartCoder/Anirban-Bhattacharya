# Generated by Django 4.0.6 on 2022-08-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnirbanBhattacharyaWebsite', '0010_ip_blogslug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(default='', max_length=100)),
                ('Phone', models.CharField(default='', max_length=15)),
                ('Service', models.CharField(default='', max_length=50)),
                ('Subject', models.CharField(default='', max_length=500)),
                ('Message', models.TextField(default='', max_length=50000)),
            ],
        ),
    ]