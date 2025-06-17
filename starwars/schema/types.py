from graphene_django.types import DjangoObjectType
from starwars.models import Character, Movie, Planet

class CharacterType(DjangoObjectType):
    """GraphQL type for the Character model.

    Inherits from DjangoObjectType and exposes all fields of the Character model.
    """

    class Meta:
        model = Character
        fields = "__all__"


class MovieType(DjangoObjectType):
    """GraphQL type for the Movie model.

    Inherits from DjangoObjectType and exposes all fields of the Movie model.
    """

    class Meta:
        model = Movie
        fields = "__all__"


class PlanetType(DjangoObjectType):
    """GraphQL type for the Planet model.

    Inherits from DjangoObjectType and exposes all fields of the Planet model.
    """

    class Meta:
        model = Planet
        fields = "__all__"
