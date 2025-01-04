from django.core.validators import MinLengthValidator
from django.db import models

from wos_app.common.validators import UserNameValidator, AgeValidator


class UserProfile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 3

    MAX_LENGTH_PASSWORD = 20

    MAX_LENGTH_NAME = 15

    ERROR_MESSAGE_USERNAME = "Username must be at least 3 chars long!"

    HELP_TEXT_AGE = "Age requirement: 21 years and above."

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_LENGTH_USERNAME, message=ERROR_MESSAGE_USERNAME),
            UserNameValidator(),
        ],
    ),
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        blank=False,
        null=False,
        help_text="Age requirement: 21 years and above.",
        validators=[
            AgeValidator(),
        ]
    ),
    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        blank=False,
        null=False,
    ),
    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=True,
        null=True,
    ),
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=True,
        null=True,
    ),
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
