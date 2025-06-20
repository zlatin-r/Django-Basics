from django.core.validators import MinLengthValidator
from django.db import models

from author.models import Author


class Post(models.Model):
    MAX_LEN_TITLE = 50
    MIN_LEN_TITLE = 5

    title = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=MAX_LEN_TITLE,
        validators=[
            MinLengthValidator(MIN_LEN_TITLE),
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        help_text="Share your funniest furry photo URL!"
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now=True
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )