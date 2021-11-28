# README
Django back, React+TypeScript front, Postgres database.

## Create Postgres database and user
0. `CREATE DATABASE {database};`
1. `CREATE USER {user} WITH PASSWORD '{password}';`
2. `ALTER ROLE {user} SET client_encoding TO 'utf8';
    ALTER ROLE {user} SET default_transaction_isolation TO 'read committed';
    ALTER ROLE {user} SET timezone TO 'UTC';`

## Setting up virtual python environment
0. `mkdir {project}`
0. `cd {project}`
~0. `virtualenv env`~
0. `python3 -m env {/path/to/new/virtual/environment}`
0. `source env/bin/activate`
0. Install django and psycopg2: `pip install django psycopg2`

## Setting up Django Project and App
0. Create Django project_folder: `django-admin stratproject {django_app_project}`
0. CD into the project: `cd django_app_project`
0. Create an app inside the project: `django-admin startapp {app_name}`
0. Register the app in `django_app/settings.py`

## Configure Django for Postgres
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': {database},
        'USER': {user},
        'PASSWORD': {password},
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### Make migrations
```
python manage.py makemigrations database_app
```
```
python manage.py migrate database_app
```

### create superuser
```
python manage.py createsuperuser
```

