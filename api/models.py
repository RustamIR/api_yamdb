from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator
from titles.models import Titles


class Review(models.Model):
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True,)
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="aut_review")
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    title = models.ForeignKey(Titles,
                              blank=True,
                              on_delete=models.CASCADE,
                              related_name="tit_review")


    def __str__(self):
       return self.text
   # class Meta:
  #      ordering = ['pub_date']


class Comment(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="comment")
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name="comment")
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
       return self.text
    #class Meta:
   #    ordering = ["pub_date"]