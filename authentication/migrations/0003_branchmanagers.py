# Generated by Django 4.0.4 on 2022-12-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchManagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]