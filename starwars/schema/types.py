from graphene_django.types import DjangoObjectType
from starwars.models import Character, Movie, Planet
from graphene import relay


class CharacterType(DjangoObjectType):
    """GraphQL type for the Character model.

    Inherits from DjangoObjectType and exposes all fields of the Character model.
    """

    class Meta:
        model = Character
        interfaces = (relay.Node,)
        fields = "__all__"
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }


class MovieType(DjangoObjectType):
    """GraphQL type for the Movie model.

    Inherits from DjangoObjectType and exposes all fields of the Movie model.
    """

    class Meta:
        model = Movie
        interfaces = (relay.Node,)
        fields = "__all__"
        filter_fields = {
            "title": ["exact", "icontains"]
        }


class PlanetType(DjangoObjectType):
    """GraphQL type for the Planet model.

    Inherits from DjangoObjectType and exposes all fields of the Planet model.
    """

    class Meta:
        model = Planet
        interfaces = (relay.Node,)
        fields = "__all__"
        filter_fields = ['name']
