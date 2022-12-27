# Generated by Django 4.0.4 on 2022-11-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainees_general',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('course_learning', models.CharField(max_length=50)),
                ('course_duration', models.CharField(max_length=50)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('location', models.CharField(max_length=50)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users')),
            ],
        ),
    ]
