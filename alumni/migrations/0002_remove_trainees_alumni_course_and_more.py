# Generated by Django 4.0.4 on 2023-01-05 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainees_alumni',
            name='course',
        ),
        migrations.RemoveField(
            model_name='trainees_alumni',
            name='course_duration',
        ),
    ]
