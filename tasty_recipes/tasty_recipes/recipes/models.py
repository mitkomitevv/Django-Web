from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from tasty_recipes.recipes.choices import CuisineTypeChoices


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 10

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[MinLengthValidator(TITLE_MIN_LENGTH)],
        unique=True,
        error_messages={'unique': "We already have a recipe with the same title!"}
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
        verbose_name="Cuisine Type"
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Provide the cooking time in minutes.",
        verbose_name="Cooking Time"
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Image URL"
    )

    author = models.ForeignKey(
        'user_profile.Profile',
        on_delete=models.CASCADE,
        related_name='recipes'
    )
