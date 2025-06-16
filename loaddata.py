# load_data.py
import requests
from starwars.models import Movie, Character, Planet
from datetime import datetime


def load_characters():
    print("Loading characters...")
    url = "https://www.swapi.tech/api/people"
    while url:
        res = requests.get(url)
        data = res.json()
        for item in data["results"]:
            Character.objects.get_or_create(name=item["name"])
        url = data["next"]



def load_planets():
    print("Loading planets...")
    url = "https://www.swapi.tech/api/planets"
    while url:
        res = requests.get(url)
        data = res.json()
        for item in data["results"]:
            detail = requests.get(item["url"]).json()
            props = detail["result"]["properties"]
            Planet.objects.get_or_create(name=props["name"], climate=props.get("climate", "unknown"))
        url = data["next"]





def load_movies():
    print("Loading movies...")
    url = "https://www.swapi.tech/api/films"
    res = requests.get(url).json()
    for film in res["result"]:
        props = film["properties"]
        movie, _ = Movie.objects.get_or_create(
            title=props["title"],
            opening_crawl=props["opening_crawl"],
            director=props["director"],
            producers=props["producer"],
            release_date=datetime.strptime(props["release_date"], "%Y-%m-%d").date()
        )

        for planet_url in props["planets"]:
            planet_id = planet_url.rstrip("/").split("/")[-1]
            planet = Planet.objects.filter(id=planet_id).first()
            if planet:
                movie.planets.add(planet)

        for character_url in props["characters"]:
            char_id = character_url.rstrip("/").split("/")[-1]
            character = Character.objects.filter(id=char_id).first()
            if character:
                character.movies.add(movie)
