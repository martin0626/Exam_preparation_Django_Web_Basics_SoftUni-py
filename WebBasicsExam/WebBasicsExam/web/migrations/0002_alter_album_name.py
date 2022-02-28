# Generated by Django 4.0.2 on 2022-02-27 09:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Ensure this value contains only letters, numbers, and underscore.', regex='^[A-Za-z0-9_\\s]*$')]),
        ),
    ]
