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
    book = models.CharField(max_length = 200)
    music = models.FileField()
    film = models.FileField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, blank=False)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1450), max_value_current_year])
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name="titles_of_category",
        blank=True,
        null=True,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name="titles_of_genre",
        blank=True,
        null=True,
    )


class Users(models.Model):
    name = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='users', 
        blank=True,
        null=True
    )
    contact = models.EmailField(max_length=50)


class Film(models.Model):
    film = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="films")
    contact = models.EmailField(max_length=50)

    def __str__(self):
        return self.film


class Book(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    contact = models.EmailField(max_length=50)
    #image = models.ImageField(upload_to='posts/', null=True, blank=True)  # поле для картинки

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)


class Review(models.Model):
