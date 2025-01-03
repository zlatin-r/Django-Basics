from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.profiles.models import Profile
from fruitipedia_app.validators import OnlyLettersValidator


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator()
        ],
        error_messages={
            'unique': "This fruit name is already in use! Try a new one.",
        },
        unique=True,
        blank=False,
        null=False,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

