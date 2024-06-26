# Generated by Django 4.1 on 2024-03-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boulders', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='boulder',
            constraint=models.UniqueConstraint(fields=('boulder_name', 'wall'), name='unique_boulder_name_per_wall'),
        ),
    ]
