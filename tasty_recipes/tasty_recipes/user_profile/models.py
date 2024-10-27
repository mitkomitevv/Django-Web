from django.core.validators import MinLengthValidator
from django.db import models
from tasty_recipes.user_profile.validators import NameCapitalizationValidator


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(
                2,
                message="Nickname must be at least 2 chars long!"
            )
        ],
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            NameCapitalizationValidator()
        ],
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            NameCapitalizationValidator()
        ],
        verbose_name="Last Name"
    )

    chef = models.BooleanField(
        default=False
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'