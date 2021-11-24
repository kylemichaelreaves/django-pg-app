# README
Django back, React+TypeScript front, Postgres database.

## Create Postgres database and user
0. `CREATE DATABASE django_postgres_app;`
1. `CREATE USER kyle_admin WITH PASSWORD 'kyle_admin_password';`
2. `ALTER ROLE kyle_admin SET client_encoding TO 'utf8';
    ALTER ROLE kyle_admin SET default_transaction_isolation TO 'read committed';
    ALTER ROLE kyle_admin SET timezone TO 'UTC';`

## Setting up virtual python environment
0. `mkdir {project}`
0. `cd {project}`
~0. `virtualenv venv`~
0. `python3 -m venv {/path/to/new/virtual/environment}`
0. `source venv/bin/activate`
0. Install django and psycopg2: `pip install django psycopg2`

## Setting up Django Project and App
0. Create Django project_folder: `django-admin stratproject {django_app_project}`
0. CD into the project: `cd django_app_project`
0. Create an app inside the project: `django-admin startapp {app_name}`
0. Register the app in `django_app/settings.py`

## Create the React frontend with CreateReactApp
0. Create a directory for the frontend: `mkdir react-frontend`
1. CD into the frontend directory`cd react-frontend`
2. Use yarn to install a React app with a TypeScript template: `yarn create react-app {app-name} --template typescript`
