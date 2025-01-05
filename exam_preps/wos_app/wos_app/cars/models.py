from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from wos_app.cars.type_choices import CarTypeChoices
from wos_app.common.validators import CarYearValidator
from wos_app.user_profile.models import UserProfile


class Car(models.Model):
    MAX_LEN_TYPE = 10

    MAX_LEN_MODEL = 15
    MIN_LEN_MODEL = 1

    MIN_YEAR = 1999
    MAX_YEAR = 2030

    MIN_PRICE = 1.0

    ERROR_MESSAGE_YEAR = f"Year must be between {MIN_YEAR} and {MAX_YEAR}!"
    ERROR_MESSAGE_UNIQUE = "This image URL is already in use! Provide a new one."

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=CarTypeChoices,
        blank=False,
        null=False,
    )
    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_LEN_MODEL)
        ],
    )
    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            CarYearValidator(MIN_YEAR, MAX_YEAR, ERROR_MESSAGE_YEAR),
        ],
    )
    image_url = models.URLField(
        unique=True,
        blank=False,
        null=False,
        error_messages={
            'unique': ERROR_MESSAGE_UNIQUE,
        },
        # TODO ADD PLACEHOLDER "https://..."
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ]
    )
    owner = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE
    )
