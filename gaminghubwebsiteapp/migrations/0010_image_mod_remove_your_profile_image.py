# Generated by Django 4.2.2 on 2023-09-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaminghubwebsiteapp', '0009_alter_your_profile_con'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_image/%y')),
            ],
        ),
        migrations.RemoveField(
            model_name='your_profile',
            name='image',
        ),
    ]
