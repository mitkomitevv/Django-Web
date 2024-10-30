from django.db import models


class PlantTypeChoices(models.TextChoices):
    OUTDOOR_PLANTS = 'Outdoor Plants', 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants', 'Indoor Plants'