from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.user_profile.validators import NameCapitalValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2),
        ]
    )

    first_name = models.CharField(
        max_length=20,
        validators=[
            NameCapitalValidator()
        ],
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=20,
        validators=[
            NameCapitalValidator()
        ],
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'