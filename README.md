# 🌌 StarWars GraphQL API

> Proyecto basado en Django + Graphene para exponer datos del universo de Star Wars a través de GraphQL.

---

## 🚀 Tecnologías

- Python 3.11+
- Django 5.2
- GraphQL con [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
- SQLite (Por temas practicos y de ejecucion)
- Pytest + pytest-django
- Requests (carga inicial de datos desde API externa SWAPI)
- Documentacion por GraphiQL. [Ver](http://127.0.0.1:8000/graphql/)

---

## 📁 Estructura del Proyecto
![image](https://github.com/user-attachments/assets/1c05a0ae-68c7-4e71-b9c6-fe9a4533d60a)


---

## ⚙️ Instalación

```bash
# Clonar repositorio
git clone https://github.com/JeissonRuiz02/StarWarsUniverse.git
cd starwars-graphql-api

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Cargar datos iniciales desde la API SWAPI
python manage.py loaddata

# Ejecutar servidor
python manage.py runserver
```
---
## 🔍 GraphQL Playground
Una vez iniciado el servidor, accede a:

http://127.0.0.1:8000/graphql/

![image](https://github.com/user-attachments/assets/423e62ae-53f2-423d-b269-ab260080862e)


---
## Simulacion de PR:
![image](https://github.com/user-attachments/assets/2dcf7669-8419-4eee-9eef-067b733e9c8a)

---

## 🧪 Ejemplos de Queries

### Obtener todos los personajes con las peliculas donde aparecen y sus respectivos planetas

```graphql
query {
  allCharacters {
    id
    name
    movies {
      title
      openingCrawl
      planets{
        name
      }
    }
  }
}
```
![image](https://github.com/user-attachments/assets/3a1ce5af-954a-4ca4-9800-971f1f530f4c)


### Filtrar personajes por nombre

```graphql
query {
  allCharacters(name: "Luke") {
    id
    name
  }
}
```
![image](https://github.com/user-attachments/assets/ac56bc56-5c13-4711-86d2-2afec3e88dc1)


### Detalles de una película

```graphql
query {
  movie(id: 1) {
    title
    director
    openingCrawl
    planets {
      name
    }
  }
}
```
![image](https://github.com/user-attachments/assets/c374d7d7-c9d0-4c4f-b23d-ba51ab4692b5)


## ✍️ Mutaciones

### Crear un personaje

```graphql
mutation {
  createCharacter(name: "Han Solo") {
    character {
      id
      name
    }
  }
}
```
![image](https://github.com/user-attachments/assets/7a94e036-9379-4b65-8f0f-d51f135e6077)


### Crear una pelicula

```graphql
mutation {
  createMovie(
    title: "The Empire Strikes Back",
    openingCrawl: "It is a dark time for the Rebellion...",
    director: "Irvin Kershner",
    producers: "George Lucas",
    releaseDate: "1980-05-21",
    planetIds: [1, 2]
  ) {
    movie {
      id
      title
    }
  }
}

```
![image](https://github.com/user-attachments/assets/d14ab8b5-fbba-48a8-84a0-a6292e4e35b8)

### Crear un planeta

```graphql
mutation {
  createPlanet(name: "Hoth", climate: "Frozen") {
    planet {
      id
      name
    }
  }
}

```
![image](https://github.com/user-attachments/assets/6b20059f-58c1-49f3-97bb-7001f29ad108)


## 🧪 Pruebas
Ejecutar pruebas unitarias:

```bash
 pytest
```
Los tests se encuentran en `starwars/tests/test_graphql.py` y validan mutaciones y queries del esquema.


## ⭐ Autor
- [**Jeisson Ruiz**](https://github.com/JeissonRuiz02)
