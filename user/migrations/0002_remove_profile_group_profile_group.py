# Generated by Django 5.0.6 on 2024-06-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.CharField(choices=[('CANDIDATE', 'Candidate'), ('COMPANY', 'Company')], default='CANDIDATE', max_length=25),
        ),
    ]
