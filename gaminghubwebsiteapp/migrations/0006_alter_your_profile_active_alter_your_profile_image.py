# Generated by Django 4.2.2 on 2023-09-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaminghubwebsiteapp', '0005_alter_your_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='your_profile',
            name='active',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='your_profile',
            name='image',
            field=models.FileField(default=None, upload_to='static/media'),
        ),
    ]