from django.core.validators import MinLengthValidator
from django.db import models
from fruitpedia.fruit.validators import FruitNameValidator
from fruitpedia.user_profile.models import Profile


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            FruitNameValidator()
        ],
        unique=True,
        error_messages={
            'unique': "This fruit name is already in use! Try a new one."
        }
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='fruits',
    )
