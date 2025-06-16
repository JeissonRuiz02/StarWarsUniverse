from graphene_django.types import DjangoObjectType
from starwars.models import Character, Movie, Planet

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = "__all__"

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = "__all__"

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = "__all__"
