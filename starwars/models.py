from django.db import models

class Planet(models.Model):
    """Model representing a planet in the Star Wars universe.

    Attributes:
        name (str): The name of the planet.
        climate (str): A description of the planet's climate.
    """

    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Returns the string representation of the planet."""
        return self.name

class Movie(models.Model):
    """Model representing a movie in the Star Wars universe.

    Attributes:
        title (str): Title of the movie.
        opening_crawl (str): The introductory crawl text shown at the beginning of the movie.
        director (str): The director of the movie.
        producers (str): The producers of the movie, stored as a comma-separated string.
        release_date (date): The official release date of the movie.
        planets (ManyToMany): The planets featured in the movie.
    """

    title = models.CharField(max_length=200)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=255)
    release_date = models.DateField()
    planets = models.ManyToManyField(Planet, related_name='movies')

    def __str__(self) -> str:
        """Returns the string representation of the movie."""
        return self.title


class Character(models.Model):
    """Model representing a character in the Star Wars universe.

    Attributes:
        name (str): The character's name.
        movies (ManyToMany): The movies the character appears in.
    """

    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='characters')

    def __str__(self) -> str:
        """Returns the string representation of the character."""
        return self.name
