from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app.profiles.validators import validate_username


class Profile(models.Model):
    MAX_NAME_LENGTH = 15
    MIN_NAME_LENGTH = 2

    username = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validate_username,
            MinLengthValidator(MIN_NAME_LENGTH)
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
