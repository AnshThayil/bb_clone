# Generated by Django 4.1 on 2024-03-27 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='num_walls',
        ),
    ]
