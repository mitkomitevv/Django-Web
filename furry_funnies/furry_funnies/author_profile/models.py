from django.core.validators import MinLengthValidator
from django.db import models
from furry_funnies.author_profile.validators import AuthorNameValidator, AuthorPasscodeValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            AuthorNameValidator()
        ],
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            AuthorNameValidator()
        ],
        verbose_name="Last Name"
    )

    passcode = models.CharField(
        validators=[
            AuthorPasscodeValidator()
        ],
        help_text="Your passcode must be a combination of 6 digits"
    )

    pets_number = models.PositiveSmallIntegerField(
        verbose_name='Pets Number'
    )

    info = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name="Profile Image URL"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"