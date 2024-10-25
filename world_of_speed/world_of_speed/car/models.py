from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from world_of_speed.car.choices import CarTypeChoice


class Car(models.Model):
    YEAR_ERROR_MESSAGE = "Year must be between 1999 and 2030!"

    type = models.CharField(
        max_length=10,
        choices=CarTypeChoice.choices
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1999, message=YEAR_ERROR_MESSAGE),
            MaxValueValidator(2030, message=YEAR_ERROR_MESSAGE),
        ]
    )

    image_url = models.URLField(
        unique=True,
        verbose_name="Image URL",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ])

    owner = models.ForeignKey(
        'user_profile.Profile',
        on_delete=models.CASCADE,
        related_name='cars'
    )