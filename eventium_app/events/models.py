from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from organizer.models import Organizer


class Events(models.Model):
    MAX_LENGTH=120
    MIN_LENGTH=2
    MIN_VALUE=0

    slogan = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
        validators=[
            MinLengthValidator(MIN_LENGTH),
        ]
    )

    location = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
        validators=[
            MinLengthValidator(MIN_LENGTH)
        ]
    )

    start_time = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now
    )

    available_tickets = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_VALUE)
        ],
    )

    key_features = models.TextField(
        null=True,
        blank=True,
    )

    banner_url = models.URLField(
        null=True,
        blank=True,
    )

    organizer = models.ForeignKey(
        to=Organizer,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-start_time"]
