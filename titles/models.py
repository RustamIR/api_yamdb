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

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=200, blank=False)
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1450), max_value_current_year])
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    genre = models.ManyToManyField(Genres, blank=True,
                                   null=True, verbose_name='Жанр')
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]
