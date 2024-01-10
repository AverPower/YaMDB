from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['name']
