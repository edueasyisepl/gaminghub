# Generated by Django 4.2.2 on 2023-09-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='your_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40)),
                ('state', models.CharField(default=None, max_length=60)),
                ('city', models.CharField(default=None, max_length=60)),
                ('image', models.FileField(default=None, upload_to='static')),
                ('full_name', models.CharField(default=None, max_length=255)),
                ('title', models.CharField(default=None, max_length=50)),
                ('date_birth', models.DateField(default=None)),
                ('con', models.TextField(default=None)),
                ('phone', models.BigIntegerField(default=None)),
            ],
        ),
    ]