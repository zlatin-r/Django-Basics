from django.contrib.auth.management.commands.createsuperuser import PASSWORD_FIELD
from django.core.validators import MinLengthValidator
from django.db import models
from django.forms.widgets import PasswordInput

from author.validators import NameValidator, PasswordLenValidator


class Author(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=40,
        validators=[
            MinLengthValidator(4),
            NameValidator(),
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        validators=[
            MinLengthValidator(2),
            NameValidator(),
        ]
    )

    passcode = models.CharField(
        max_length=6,
        help_text="Your passcode must be a combination of 6 digits",
        validators=[
            PasswordLenValidator(),
        ]
    )

    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
