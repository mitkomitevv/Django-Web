# Generated by Django 5.1.2 on 2024-10-23 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_url',
            field=models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1999, message='Year must be between 1999 and 2030!'), django.core.validators.MaxValueValidator(2030, message='Year must be between 1999 and 2030!')]),
        ),
    ]
