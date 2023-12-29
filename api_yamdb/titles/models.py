from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
