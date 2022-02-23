from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    NAME_MAX_LEN = 20
    AGE_MIN_VALUE = 0
    AGE_MAX_VALUE = 120

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    age = models.IntegerField(
        validators=[
            MinValueValidator(AGE_MIN_VALUE),
            MaxValueValidator(AGE_MAX_VALUE),
            ]
    )

    image_url = models.URLField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    image_url = models.URLField()
    content = models.TextField()
