# Generated by Django 4.0.6 on 2022-07-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnirbanBhattacharyaWebsite', '0007_alter_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
    ]