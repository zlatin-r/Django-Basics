from django.core.validators import MinValueValidator
from django.db import models

from music_app.albums.chioces import GenreChoices
from music_app.profiles.models import Profile


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    MIN_PRICE = 0.0

    album_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )
