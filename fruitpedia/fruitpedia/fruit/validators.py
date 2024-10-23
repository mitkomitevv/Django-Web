from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FruitNameValidator:
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError('Fruit name should contain only letters!')
