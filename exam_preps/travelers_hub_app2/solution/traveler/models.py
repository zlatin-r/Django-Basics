from django.core.validators import MinLengthValidator
from django.db import models

from traveler.validators import NicknameValidator


class Traveler(models.Model):
    MAX_LENGTH = 30
    MIN_LENGTH = 3

    nickname = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
        help_text="Nicknames can contain only letters and digits.",
        validators=[
            MinLengthValidator(MIN_LENGTH),
            NicknameValidator()
        ],
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=MAX_LENGTH,
    )

    country = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_LENGTH)
        ]
    )

    about_me = models.TextField(
        null=True,
        blank=True
    )
