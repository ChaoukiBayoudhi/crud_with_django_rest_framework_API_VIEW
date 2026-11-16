# Crud with Django REST framework API VIEW

A Django project with 1 model and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- django-cors-headers
- psycopg2 (PostgreSQL)
- Pillow
- Database: SQLite

## Project structure

- `crud_with_django_rest_framework/`: project settings and root URLs
- `player_app/`: Django app
- Tests: `player_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Player` | `player_app` | name, birthDate, country, email, tshirtNumber, photo |

## URL routes

Declared in `urls.py`:

- `/blog/`
- `/api/`
- `/^api/players$`
- `/^api/players/(?P<pk>[0-9]+)$`
- `/^api/players/agegte/(?P<pk>[0-9]+)/$`
- `/players/`
- `/players/<int:pk>/`
- `/players/agegte/<int:age_seuil>`

## How to run

```bash
pip install pipenv
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
