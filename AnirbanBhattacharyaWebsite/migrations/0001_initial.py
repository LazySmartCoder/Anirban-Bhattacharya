# Generated by Django 4.0.6 on 2022-07-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=40)),
                ('Email', models.EmailField(default='', max_length=200)),
                ('Subject', models.CharField(default='', max_length=50)),
                ('Message', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
