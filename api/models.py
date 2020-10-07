from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator
from titles.models import Titles


class Review(models.Model):
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="review")
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    title = models.ForeignKey(Titles,
                              blank=True,
                              on_delete=models.CASCADE,
                              related_name="review")

    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="comment")
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name="comment")
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["pub_date"]