from django.core.validators import MinLengthValidator
from django.db import models
from my_plant_app.plant.choices import PlantTypeChoices
from my_plant_app.plant.validators import PlantNameValidator


class Plant(models.Model):
    plant_type = models.CharField(
        max_length=14,
        choices=PlantTypeChoices.choices,
        verbose_name='Type'
    )

    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            PlantNameValidator()
        ]
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField()

    price = models.FloatField()