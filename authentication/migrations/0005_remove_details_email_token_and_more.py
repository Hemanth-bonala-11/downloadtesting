# Generated by Django 4.2.4 on 2023-08-09 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_details_email_token_details_is_verified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='email_token',
        ),
        migrations.RemoveField(
            model_name='details',
            name='is_verified',
        ),
    ]
