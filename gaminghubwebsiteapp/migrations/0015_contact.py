# Generated by Django 4.2.2 on 2023-09-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaminghubwebsiteapp', '0014_otp_verify_registered_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=60)),
                ('last_name', models.CharField(default=None, max_length=60)),
                ('email_address', models.EmailField(default=None, max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]