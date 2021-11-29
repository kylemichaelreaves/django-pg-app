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
0. `python3 -m venv {/path/to/new/virtual/environment}`
  0. It's possible to update the version of the python venv with this command, where `venv` is the path to the direcotry: `python3 -m venv --upgrade venv`
0. `source venv/bin/activate`
0. Install django and psycopg2: `pip install django psycopg2 djangorestframework django-cors-headers`

## Setting up Django Project and App
0. Create Django project_folder: `django-admin stratproject {django_app_project}`
0. CD into the project: `cd {django_app_project}`
0. Create an app inside the project: `django-admin startapp {app_name}`
0. Register the app, djangorestframework, and django-cors-headers in `django_app/settings.py`

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

## Create the React frontend with CreateReactApp
0. Create a directory for the frontend: `mkdir react-frontend`
1. CD into the frontend directory`cd react-frontend`
2. Use yarn to install a React app with a TypeScript template: `yarn create react-app {app-name} --template typescript`

### add react-bootstrap
```
cd react-frontend
npm i react-bootstrap bootstrap@5.1.3
```
## If Git says, "Your configuration specificies to me with the ref <branch> from the remote but no such ref was fetched.":
```
git fetch --prune origin
git branch --unset-upstream
```
