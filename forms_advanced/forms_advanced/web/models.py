from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_first_name(value):
    if " " in value:
        raise ValidationError("First name should not contain spaces.")


class Person(models.Model):
    first_name = models.CharField(
        max_length=32,
        validators=(
            validate_first_name,
            MinLengthValidator(1)
        )
    )
