# Generated by Django 4.2.4 on 2023-08-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstNname', models.CharField(max_length=122)),
                ('lastName', models.CharField(max_length=122)),
                ('mailId', models.EmailField(max_length=122)),
                ('phoneNumber', models.IntegerField(max_length=15)),
                ('password', models.CharField(max_length=122)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
