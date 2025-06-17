import graphene
from datetime import datetime
from starwars.models import Character, Movie, Planet
from starwars.schema.types import CharacterType, MovieType, PlanetType


class CreateCharacter(graphene.Mutation):
    """GraphQL mutation to create a new Character."""

    class Arguments:
        name = graphene.String(required=True)

    character = graphene.Field(CharacterType)

    def mutate(self, info, name):
        """
        Create a new character with the given name.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            name (str): Name of the character to create.

        Returns:
            CreateCharacter: The mutation result containing the created character.
        """
        character = Character.objects.create(name=name)
        return CreateCharacter(character=character)


class CreatePlanet(graphene.Mutation):
    """GraphQL mutation to create a new Planet."""

    class Arguments:
        name = graphene.String(required=True)
        climate = graphene.String(required=True)

    planet = graphene.Field(PlanetType)

    def mutate(self, info, name, climate):
        """
        Create a new planet with the given name and climate.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            name (str): Name of the planet.
            climate (str): Climate description of the planet.

        Returns:
            CreatePlanet: The mutation result containing the created planet.
        """
        planet = Planet.objects.create(name=name, climate=climate)
        return CreatePlanet(planet=planet)


class CreateMovie(graphene.Mutation):
    """GraphQL mutation to create a new Movie."""

    class Arguments:
        title = graphene.String(required=True)
        opening_crawl = graphene.String(required=True)
        director = graphene.String(required=True)
        producers = graphene.String(required=True)
        release_date = graphene.String(required=True)  # Expected in ISO format: YYYY-MM-DD
        planet_ids = graphene.List(graphene.ID)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, opening_crawl, director, producers, release_date, planet_ids=[]):
        """
        Create a new movie and associate it with the given planets.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            title (str): Title of the movie.
            opening_crawl (str): Intro text of the movie.
            director (str): Name of the director.
            producers (str): Comma-separated list of producers.
            release_date (str): Release date in 'YYYY-MM-DD' format.
            planet_ids (List[str]): List of Planet IDs to associate with the movie.

        Returns:
            CreateMovie: The mutation result containing the created movie.
        """
        movie = Movie.objects.create(
            title=title,
            opening_crawl=opening_crawl,
            director=director,
            producers=producers,
            release_date=datetime.strptime(release_date, "%Y-%m-%d").date()
        )
        movie.planets.set(Planet.objects.filter(id__in=planet_ids))
        return CreateMovie(movie=movie)


class Mutation(graphene.ObjectType):
    """Root GraphQL mutation object exposing all available mutations."""

    create_character = CreateCharacter.Field()
    create_planet = CreatePlanet.Field()
    create_movie = CreateMovie.Field()
