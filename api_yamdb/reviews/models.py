from django.db import models

from api.models import User
from titles.models import Title


SCORE_CHOICES = zip(range(1, 11), range(1, 11))


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORE_CHOICES)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_date', )
        unique_together = ('author', 'title')


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_date', )
