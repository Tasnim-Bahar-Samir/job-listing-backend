# Generated by Django 5.0.6 on 2024-06-14 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_savedjob'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SavedJob',
        ),
    ]
