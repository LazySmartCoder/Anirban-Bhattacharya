# Generated by Django 5.0.1 on 2024-02-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AnirbanBhattacharyaWebsite", "0021_rename_photos_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="Image",
            field=models.ImageField(
                max_length=1000, upload_to="RequiredImages/PersonalPhotos"
            ),
        ),
    ]
