from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.user_profile.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message='Username must be at least 3 chars long!'),
            UsernameValidator()
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(21)
        ],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        max_length=20
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )
