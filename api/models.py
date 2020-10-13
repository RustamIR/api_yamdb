from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator
from titles.models import Titles


class Review(models.Model):
    text = models.TextField(blank=False, verbose_name='Отзыв')
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="aut_review", verbose_name='Автор')
    score = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(10)],
                                        verbose_name='Оценка')
    title = models.ForeignKey(Titles,
                              blank=True,
                              on_delete=models.CASCADE,
                              related_name="reviews",
                              verbose_name='Дата публикации')


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('author', 'title')
        ordering = ["pub_date"]

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="comment", verbose_name='Автор')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name="comment", verbose_name='Отзыв', )
    text = models.TextField(blank=False, verbose_name='Комментарий')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')

    class Meta:
        ordering = ["pub_date"]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text

