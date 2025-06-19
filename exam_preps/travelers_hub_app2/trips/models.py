from django.core.validators import MinLengthValidator
from django.db import models
from traveler.models import Traveler


class Trip(models.Model):
    MAX_LENGTH = 100
    MIN_LENGTH = 3

    destination = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
        validators=[
            MinLengthValidator(MIN_LENGTH),
        ]
    )

    summary = models.TextField(
        null=False,
        blank=False
    )

    start_date = models.DateField(
        null=False,
        blank=False,
    )

    duration = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        default=1,
        help_text="Duration in days is expected."
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    traveler = models.ForeignKey(
        to=Traveler,
        on_delete=models.CASCADE,

    )
