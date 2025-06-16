import graphene
from starwars.schema.mutations import Mutation
from .queries import Query



schema = graphene.Schema(query=Query, mutation=Mutation)
