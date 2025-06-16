import graphene
from starwars.models import Character, Movie, Planet
from starwars.schema.types import CharacterType, MovieType, PlanetType

class Query(graphene.ObjectType):
    character = graphene.Field(CharacterType, id=graphene.ID(required=True))
    movie = graphene.Field(MovieType, id=graphene.ID(required=True))
    planet = graphene.Field(PlanetType, id=graphene.ID(required=True))

    all_characters = graphene.List(CharacterType, name=graphene.String())
    all_movies = graphene.List(MovieType)
    all_planets = graphene.List(PlanetType)
    movies_by_title = graphene.List(MovieType, title=graphene.String())
    planets_by_name = graphene.List(PlanetType, name=graphene.String())

    def resolve_character(self, info, id):
        return Character.objects.get(pk=id)

    def resolve_movie(self, info, id):
        return Movie.objects.get(pk=id)

    def resolve_planet(self, info, id):
        return Planet.objects.get(pk=id)

    def resolve_all_characters(self, info, name=None):
        qs = Character.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
        return qs

    def resolve_all_movies(self, info):
        return Movie.objects.all()

    def resolve_all_planets(self, info):
        return Planet.objects.all()

    def resolve_movies_by_title(self, info, title=None):
        qs = Movie.objects.all()
        if title:
            qs = qs.filter(title__icontains=title)
        return qs

    def resolve_planets_by_name(self, info, name=None):
        qs = Planet.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
        return qs
