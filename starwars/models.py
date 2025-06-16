from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=255)
    release_date = models.DateField()
    planets = models.ManyToManyField(Planet, related_name='movies')

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='characters')

    def __str__(self):
        return self.name