from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from DjangoExamPrep01.Expenses.validators import only_letters_validator, MaxSizeImageFieldValidator


class Profile(models.Model):
    MAX_LEN_NAME = 15
    MIN_LEN_NAME = 2

    MIN_VALUE_BUDGET = 0
    MAX_SIZE_IMAGE = 5

    first_name = models.CharField(
        max_length= MAX_LEN_NAME,
        validators=[MinLengthValidator(MIN_LEN_NAME), only_letters_validator],
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=[MinLengthValidator(MIN_LEN_NAME), only_letters_validator],
    )

    budget = models.FloatField(
        default=0,
        validators=[MinValueValidator(MIN_VALUE_BUDGET)],
    )

    image = models.ImageField(
        blank=True,
        null=True,
        validators=[MaxSizeImageFieldValidator(MAX_SIZE_IMAGE)],
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()
