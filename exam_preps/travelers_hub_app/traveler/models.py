from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from traveler.validators import NicknameValidator


class Traveler(models.Model):
    MAX_LENGTH = 30
    MIN_LENGTH =3

    nickname = models.CharField(
        unique=True,
        max_length=MAX_LENGTH,
        validators=(
            MinLengthValidator(MIN_LENGTH),
            NicknameValidator(),
        ),
        help_text="*Nicknames can contain only letters and digits.",
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=MAX_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )
    country = models.CharField(
        max_length=MIN_LENGTH,
        validators=(
            MaxLengthValidator(MIN_LENGTH),
        ),
        blank=False,
        null=False,
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )
