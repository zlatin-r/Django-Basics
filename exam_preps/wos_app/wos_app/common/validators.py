import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UserNameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Username must contain only letters, digits, and underscores!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not re.match(r'^[A-Za-z0-9_]+$', value):
            raise ValidationError(self.message)


@deconstructible
class AgeValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Age cannot be below 21."
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if value < 21:
            raise ValidationError(self.message)


@deconstructible
class CarYearValidator:
    def __init__(self, start_year, end_year, message=None):
        self.message = message
        self.start_year = start_year
        self.end_year = end_year

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Year must be between {self.start_year} and {self.end_year}!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not self.start_year <= value <= self.end_year:
            raise ValidationError(self.message)
