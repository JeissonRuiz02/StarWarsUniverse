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
StarWarsUniverse/
├── starwars/ # App principal con modelos, schema, tests y carga inicial
│ ├── models.py # Modelos de Planet, Movie y Character
│ ├── schema/
│ │ ├── queries.py # Consultas GraphQL definidas (Query)
│ │ ├── mutations.py # Mutaciones GraphQL para crear registros
│ │ └── schema.py # Esquema principal de GraphQL
│ ├── management/
│ │ └── commands/
│ │ └── load_initial_data.py # Script para cargar datos desde JSON o API externa
│ └── tests/
│ └── test_graphql.py # Pruebas unitarias para queries y mutaciones
├── starwars_api/ # Configuración del proyecto Django
│ ├── settings.py # Configuraciones principales de Django
│ └── urls.py # Rutas incluyendo endpoint /graphql/
├── db.sqlite3 # Base de datos local SQLite
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación principal del proyecto

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
python manage.py load_initial_data

# Ejecutar servidor
python manage.py runserver
```
---
## 🔍 GraphQL Playground
Una vez iniciado el servidor, accede a:

http://127.0.0.1:8000/graphql/

---
## Simulacion de PR:
![image](https://github.com/user-attachments/assets/2dcf7669-8419-4eee-9eef-067b733e9c8a)

---

## 🧪 Ejemplos de Queries

### Obtener todos los personajes

```graphql
query {
  allCharacters {
    id
    name
    movies {
      title
    }
  }
}
```

### Filtrar personajes por nombre

```graphql
query {
  allCharacters(name: "Luke") {
    id
    name
  }
}
```

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


## 🧪 Pruebas
Ejecutar pruebas unitarias:

```bash
 pytest
```
Los tests se encuentran en `starwars/tests/test_graphql.py` y validan mutaciones y queries del esquema.


## ⭐ Autor
- [**Jeisson Ruiz**](https://github.com/JeissonRuiz02)
