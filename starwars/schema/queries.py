import graphene
from starwars.models import Character, Movie, Planet
from starwars.schema.types import CharacterType, MovieType, PlanetType


class Query(graphene.ObjectType):
    """
    Root GraphQL query object that defines all available read operations
    for Characters, Movies, and Planets.
    """

    # Single item queries
    character = graphene.Field(CharacterType, id=graphene.ID(required=True))
    movie = graphene.Field(MovieType, id=graphene.ID(required=True))
    planet = graphene.Field(PlanetType, id=graphene.ID(required=True))

    # List queries
    all_characters = graphene.List(CharacterType, name=graphene.String())
    all_movies = graphene.List(MovieType)
    all_planets = graphene.List(PlanetType)
    movies_by_title = graphene.List(MovieType, title=graphene.String())
    planets_by_name = graphene.List(PlanetType, name=graphene.String())

    def resolve_character(self, info, id):
        """
        Retrieve a single character by ID.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            id (str): ID of the character.

        Returns:
            Character: The requested character instance.
        """
        return Character.objects.get(pk=id)

    def resolve_movie(self, info, id):
        """
        Retrieve a single movie by ID.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            id (str): ID of the movie.

        Returns:
            Movie: The requested movie instance.
        """
        return Movie.objects.get(pk=id)

    def resolve_planet(self, info, id):
        """
        Retrieve a single planet by ID.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            id (str): ID of the planet.

        Returns:
            Planet: The requested planet instance.
        """
        return Planet.objects.get(pk=id)

    def resolve_all_characters(self, info, name=None):
        """
        Retrieve a list of all characters, optionally filtered by name.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            name (str, optional): Filter by partial name match.

        Returns:
            QuerySet: List of Character instances.
        """
        qs = Character.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
        return qs

    def resolve_all_movies(self, info):
        """
        Retrieve a list of all movies.

        Args:
            info (ResolveInfo): GraphQL resolver info.

        Returns:
            QuerySet: List of Movie instances.
        """
        return Movie.objects.all()

    def resolve_all_planets(self, info):
        """
        Retrieve a list of all planets.

        Args:
            info (ResolveInfo): GraphQL resolver info.

        Returns:
            QuerySet: List of Planet instances.
        """
        return Planet.objects.all()

    def resolve_movies_by_title(self, info, title=None):
        """
        Retrieve a list of movies, optionally filtered by title.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            title (str, optional): Filter by partial title match.

        Returns:
            QuerySet: List of Movie instances.
        """
        qs = Movie.objects.all()
        if title:
            qs = qs.filter(title__icontains=title)
        return qs

    def resolve_planets_by_name(self, info, name=None):
        """
        Retrieve a list of planets, optionally filtered by name.

        Args:
            info (ResolveInfo): GraphQL resolver info.
            name (str, optional): Filter by partial name match.

        Returns:
            QuerySet: List of Planet instances.
        """
        qs = Planet.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
        return qs
