# Generated by Django 4.0.6 on 2022-07-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnirbanBhattacharyaWebsite', '0004_remove_blog_likes_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='Likes',
            field=models.CharField(default='', max_length=10),
        ),
    ]
