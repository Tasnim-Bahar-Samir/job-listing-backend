# Generated by Django 5.0.6 on 2024-06-13 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth0', '0001_initial'),
        ('user', '0002_remove_profile_group_profile_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]