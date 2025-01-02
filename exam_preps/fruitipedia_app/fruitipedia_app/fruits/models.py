from django.core.validators import MinLengthValidator
from django.db import models

class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),

        ]
    )
