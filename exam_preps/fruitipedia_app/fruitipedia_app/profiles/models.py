from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from fruitipedia_app.validators import StartLetterValidator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            StartLetterValidator(),
        ],
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            StartLetterValidator(),
        ],
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=40,
        unique=True,
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8),
        ],
        help_text="*Password length requirements: 8 to 20 characters",
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        default=18,
        blank=True,
        null=True
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
