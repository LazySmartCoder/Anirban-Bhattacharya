# Generated by Django 4.0.6 on 2022-08-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnirbanBhattacharyaWebsite', '0009_alter_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='BlogSlug',
            field=models.CharField(default='', max_length=100),
        ),
    ]