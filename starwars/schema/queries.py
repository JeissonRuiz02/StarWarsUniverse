import graphene
from starwars.models import Character, Movie, Planet
from starwars.schema.types import CharacterType, MovieType, PlanetType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField



class Query(graphene.ObjectType):
    """
    Root GraphQL query object that defines all available read operations
    for Characters, Movies, and Planets.
    """

    node = relay.Node.Field()

    # Single item queries
    character = relay.Node.Field(CharacterType)
    movie = relay.Node.Field(MovieType)
    planet = relay.Node.Field(PlanetType)

    all_characters = DjangoFilterConnectionField(CharacterType)
    all_movies = DjangoFilterConnectionField(MovieType)
    all_planets = DjangoFilterConnectionField(PlanetType)

    @staticmethod
    def resolve_character(info, character_id):
        """
        Retrieve a single character by ID.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            character_id (str): ID of the character.

        Returns:
            Character: The requested character instance.
            :param info:
            :param character_id:
        """
        return Character.objects.get(pk=character_id)

    @staticmethod
    def resolve_movie(info, movie_id):
        """
        Retrieve a single movie by ID.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            movie_id (str): ID of the movie.

        Returns:
            Movie: The requested movie instance.
            :param info:
            :param movie_id:
        """
        return Movie.objects.get(pk=movie_id)

    @staticmethod
    def resolve_planet(info, planet_id):
        """
        Retrieve a single planet by ID.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            planet_id (str): ID of the planet.

        Returns:
            Planet: The requested planet instance.
            :param info:
            :param planet_id:
        """
        return Planet.objects.get(pk=planet_id)


