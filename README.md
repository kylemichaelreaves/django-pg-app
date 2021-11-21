# README
Django back, React+TypeScript front, Postgres database.

## Setting up virtual python environment
0. `mkdir {project}`
0. `cd {project}`
0. `virtualenv venv`
0. `source venv/bin/activate`
0. Install django and psycopg2: `pip install django psycopg2`

## Setting up Django Project and App
0. Create Django project_folder: `django-admin stratproject {django_app_project}`
0. CD into the project: `cd django_app_project`
0. Create an app inside the project: `django-admin startapp {app_name}`
0. Register the app in `django_app/settings.py`

