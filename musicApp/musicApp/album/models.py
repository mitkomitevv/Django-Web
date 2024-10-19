from django.core.validators import MinValueValidator
from django.db import models
from musicApp.album.choices import GenreChoices
from musicApp.profile_user.models import Profile


# Create your models here.
class Album(models.Model):
    MAX_LEN =30

    name = models.CharField(
        max_length=MAX_LEN,
        unique=True,
        verbose_name='Album Name'
    )

    artist_name = models.CharField(
        max_length=MAX_LEN,
        verbose_name='Artist'
    )

    genre = models.CharField(
        max_length=MAX_LEN,
        choices=GenreChoices.choices
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='albums',
    )
