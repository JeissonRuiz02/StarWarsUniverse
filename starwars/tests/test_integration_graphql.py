import pytest
from graphene.test import Client
from starwars.schema.schema import schema
from starwars.models import Planet, Movie


@pytest.mark.django_db
def test_create_movie_with_planet():
    client = Client(schema)

    mutation_planet = '''
        mutation {
            createPlanet(name: "Tatooine", climate: "Arid") {
                planet {
                    id
                    name
                }
            }
        }
    '''
    planet_result = client.execute(mutation_planet)
    assert "errors" not in planet_result, planet_result.get("errors")

    planet_id = planet_result["data"]["createPlanet"]["planet"]["id"]

    mutation_movie = f'''
        mutation {{
            createMovie(
                title: "A New Hope",
                openingCrawl: "Test crawl...",
                director: "George Lucas",
                producers: "Gary Kurtz",
                releaseDate: "1977-05-25",
                planetIds: ["{planet_id}"]
            ) {{
                movie {{
                    id
                    title
                    planets {{
                        edges {{
                            node {{
                                name
                            }}
                        }}
                    }}
                }}
            }}
        }}
    '''
    movie_result = client.execute(mutation_movie)
    assert "errors" not in movie_result, movie_result.get("errors")

    movie_data = movie_result["data"]["createMovie"]["movie"]
    assert movie_data["title"] == "A New Hope"



@pytest.mark.django_db
def test_create_character_and_query():
    client = Client(schema)

    mutation = '''
        mutation {
            createCharacter(name: "Obi-Wan Kenobi") {
                character {
                    id
                    name
                }
            }
        }
    '''
    result = client.execute(mutation)
    assert "errors" not in result, result.get("errors")

    char_id = result["data"]["createCharacter"]["character"]["id"]

    query = f'''
        query {{
            character(id: "{char_id}") {{
                id
                name
            }}
        }}
    '''
    result_query = client.execute(query)
    assert "errors" not in result_query, result_query.get("errors")
    assert result_query["data"]["character"]["name"] == "Obi-Wan Kenobi"
