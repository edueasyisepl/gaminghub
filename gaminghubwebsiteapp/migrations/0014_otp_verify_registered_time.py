# Generated by Django 4.2.2 on 2023-09-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaminghubwebsiteapp', '0013_alter_otp_verify_name_alter_otp_verify_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp_verify',
            name='registered_time',
            field=models.TimeField(default=None),
        ),
    ]
