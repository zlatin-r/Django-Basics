from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from fruitipedia_app.validators import StartLetterValidator

class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2)
        ],
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            StartLetterValidator
        ]
    )
