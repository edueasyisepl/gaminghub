# Generated by Django 4.2.2 on 2023-09-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaminghubwebsiteapp', '0006_alter_your_profile_active_alter_your_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='your_profile',
            name='active',
        ),
        migrations.AddField(
            model_name='your_profile',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
