from django.core.validators import MinLengthValidator
from django.db import models
from fruitpedia.user_profile.validators import UsernameValidator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            UsernameValidator()
        ],
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            UsernameValidator()
        ]
    )

    email = models.EmailField(
        unique=True,
        max_length=40
    )

    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text="*Password length requirements: 8 to 20 characters"
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=18
    )