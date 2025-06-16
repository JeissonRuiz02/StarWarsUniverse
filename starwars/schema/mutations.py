import graphene
from starwars.models import Character, Movie, Planet
from datetime import datetime
from starwars.schema.types import CharacterType, MovieType, PlanetType

class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    character = graphene.Field(CharacterType)

    def mutate(self, info, name):
        character = Character.objects.create(name=name)
        return CreateCharacter(character=character)

class CreatePlanet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        climate = graphene.String(required=True)

    planet = graphene.Field(PlanetType)

    def mutate(self, info, name, climate):
        planet = Planet.objects.create(name=name, climate=climate)
        return CreatePlanet(planet=planet)

class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        opening_crawl = graphene.String(required=True)
        director = graphene.String(required=True)
        producers = graphene.String(required=True)
        release_date = graphene.String(required=True)  # ISO format
        planet_ids = graphene.List(graphene.ID)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, opening_crawl, director, producers, release_date, planet_ids=[]):
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
    create_character = CreateCharacter.Field()
    create_planet = CreatePlanet.Field()
    create_movie = CreateMovie.Field()
