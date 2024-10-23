from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator:
    def __call__(self, value):
        if not value[0].isalpha():
            raise ValidationError('Your name must start with a letter!')
