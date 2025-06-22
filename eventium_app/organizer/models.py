from django.core.validators import MinLengthValidator
from django.db import models

from organizer.validators import NameValidator, DigitsOnlyValidator, FourUniqueDigitsValidator


class Organizer(models.Model):
    MAX_LENGTH_CN = 110
    MAX_LENGTH_PN = 15

    HELP_TEXT_CN = "*Allowed names contain letters, digits, spaces, and hyphens."
    HELP_TEXT_SK = "*Pick a combination of 4 unique digits."

    company_name = models.CharField(
        max_length=MAX_LENGTH_CN,
        unique=True,
        null=False,
        blank=False,
        help_text=HELP_TEXT_CN,
        validators=[
            MinLengthValidator(2),
            NameValidator(),
        ]
    )

    phone_number = models.CharField(
        max_length=MAX_LENGTH_PN,
        null=False,
        blank=False,
        unique=True,
        validators=[
            DigitsOnlyValidator(),
        ]
    )

    secret_key = models.CharField(
        null=False,
        blank=False,
        help_text=HELP_TEXT_SK,
        validators=[
            FourUniqueDigitsValidator(),
        ]
    )

    website = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Organizer: {self.company_name}"
