# Generated by Django 4.2.2 on 2023-09-23 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaminghubwebsiteapp', '0007_remove_your_profile_active_your_profile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp_verify',
            name='status',
        ),
    ]
