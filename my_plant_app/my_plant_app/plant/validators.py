from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PlantNameValidator:
    def __init__(self, message=None):
        self.message = message or "Plant name should contain only letters!"

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)
