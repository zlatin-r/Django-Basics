from django.core.validators import MinLengthValidator
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 chars long!")
        ]
    )
