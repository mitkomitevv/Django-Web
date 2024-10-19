from django.core.validators import MinLengthValidator
from django.db import models
from musicApp.profile_user.validators import UsernameValidator


# Create your models here.
class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2

    username = models.CharField(
        max_length = MAX_LEN_USERNAME,
        validators=[
            MinLengthValidator(MIN_LEN_USERNAME),
            UsernameValidator()
        ],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
