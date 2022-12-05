# Generated by Django 4.1.3 on 2022-12-04 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(13), django.core.validators.MinValueValidator(19)]),
        ),
    ]
