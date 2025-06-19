from django.db import models

class Traveler(models.Model):
    nickname = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30
    )
