# Generated by Django 4.0.4 on 2023-01-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainees_general',
            name='training_fee',
            field=models.DecimalField(decimal_places=2, default=100000.0, max_digits=10),
        ),
    ]
