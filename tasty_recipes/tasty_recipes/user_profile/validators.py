from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameCapitalizationValidator:
    def __init__(self, message=None):
        self.message = message or "Name must start with a capital letter!"

    def __call__(self, value):
        if not value[0].isupper():
            raise ValidationError(self.message)
