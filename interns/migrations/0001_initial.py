# Generated by Django 4.0.4 on 2022-12-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
                ('attached_area', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users')),
            ],
        ),
    ]
