import pytest
from graphene.test import Client

from starwars.models import Character
from starwars.schema.schema import schema

@pytest.mark.django_db
def test_create_character():
    client = Client(schema)
    mutation = '''
        mutation {
            createCharacter(name: "Han Solo") {
                character {
                    id
                    name
                }
            }
        }
    '''
    result = client.execute(mutation)
    assert result["data"]["createCharacter"]["character"]["name"] == "Han Solo"


@pytest.mark.django_db
def test_query_all_characters():
    Character.objects.create(name="Leia Organa")
    client = Client(schema)

    query = '''
        query {
            allCharacters(first: 5) {
                edges {
                    node {
                        name
                    }
                }
            }
        }
    '''
    result = client.execute(query)
    assert "errors" not in result, result.get("errors")

    names = [edge["node"]["name"] for edge in result["data"]["allCharacters"]["edges"]]
    assert "Leia Organa" in names