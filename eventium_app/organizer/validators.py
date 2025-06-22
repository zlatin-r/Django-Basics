import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "The company name is invalid!"

    def __call__(self, value):
        if not re.match(r'^[a-zA-Z0-9 _-]+$', value):
            raise ValidationError(self.message)


@deconstructible
class DigitsOnlyValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value or f"The field must contain digits only!"

    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError(self.message)


@deconstructible
class FourUniqueDigitsValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value or "Your secret key must have 4 unique digits!"

    def __call__(self, value):
        if not value.isdigit() or len(value) != 4 or len(set(value)) != 4:
            raise ValidationError(self.message)
