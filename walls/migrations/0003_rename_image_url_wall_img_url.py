# Generated by Django 4.1 on 2024-03-29 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walls', '0002_wall_unique_wall_name_per_gym'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wall',
            old_name='image_url',
            new_name='img_url',
        ),
    ]
