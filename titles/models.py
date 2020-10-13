from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

User = get_user_model()


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=200, blank=False)
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1450), max_value_current_year])
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name="titles_of_category",
        blank=True,
        null=True,
    )
    genre = models.ForeignKey(
        Genres,
        on_delete=models.SET_NULL,
        related_name="titles_of_genre",
        blank=True,
        null=True,
    )
