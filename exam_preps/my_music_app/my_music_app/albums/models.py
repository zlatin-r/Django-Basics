from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.profiles.models import Profile


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    MIN_PRICE = 0

    class GenreChoices(models.TextChoices):
        GENRE_POP_MUSIC = 'Pop Music', 'Pop Music'
        GENRE_JAZZ_MUSIC = 'Jazz Music', 'Jazz Music'
        GENRE_RNB_MUSIC = 'R&B Music', 'R&B Music'
        GENRE_ROCK_MUSIC = 'Rock Music', 'Rock Music'
        GENRE_COUNTRY_MUSIC = 'Country Music', 'Country Music'
        GENRE_DANCE_MUSIC = 'Dance Music', 'Dance Music'
        GENRE_HIP_HOP_MUSIC = 'Hip Hop Music', 'Hip Hop Music'
        GENRE_OTHER = 'Other', 'Other'

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GenreChoices.choices,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE),
        ],
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.DO_NOTHING,
    )