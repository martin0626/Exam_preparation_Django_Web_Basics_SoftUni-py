from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2
    AGE_MIN_VALUE = 0
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[MinLengthValidator(USERNAME_MIN_LEN)],
    )

    email = models.EmailField()
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(AGE_MIN_VALUE)],
    )


class Album(models.Model):
    NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.0

    TYPE_CHOICE_POP = 'Pop Music'
    TYPE_CHOICE_JAZZ = 'Jazz Music'
    TYPE_CHOICE_RB = 'R&B Music'
    TYPE_CHOICE_ROCK = 'Rock Music'
    TYPE_CHOICE_COUNTRY = 'Country Music'
    TYPE_CHOICE_DANCE = 'Dance Music'
    TYPE_CHOICE_HIP_HOP = 'Hip Hop Music'
    TYPE_CHOICE_OTHER = 'Other'

    GENRE_CHOICES = (
        (TYPE_CHOICE_POP, 'Pop Music'),
        (TYPE_CHOICE_JAZZ, 'Jazz Music'),
        (TYPE_CHOICE_RB, 'R&B Music'),
        (TYPE_CHOICE_ROCK, 'Rock Music'),
        (TYPE_CHOICE_COUNTRY, 'Country Music'),
        (TYPE_CHOICE_DANCE, 'Dance Music'),
        (TYPE_CHOICE_HIP_HOP, 'Hip Hop Music'),
        (TYPE_CHOICE_OTHER, 'Other'),
    )

    name = models.CharField(
        unique=True,
        max_length=NAME_MAX_LEN,
        validators=[RegexValidator(
            regex='^[A-Za-z0-9_\s]*$',
            message='Ensure this value contains only letters, numbers, and underscore.',
            )
        ]

    )
    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRE_CHOICES,
    )


    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()
    price = models.FloatField(
        validators=[MinValueValidator(PRICE_MIN_VALUE)],
    )


