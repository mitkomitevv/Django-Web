from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator:
    def __call__(self, value):
        if not all(char.isalnum() or char == '_' for char in value):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
