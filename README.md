# django-quickstart

This is a simple django quickstart project, part of AkadamiaIT initiative.

Prereguisities:
* CLI knowledge
* Docker and docker compose

Running the example:
* `docker build .`
* `docker-compose run web pipenv run django-admin startproject quickstart .`
** initial start will fail because of missing django files but will create database directories
* `docker compose up`
** will fail cause there is no project set up.
* `docker-compose run web pipenv run django-admin startproject quickstart .`
* update settings for postgreSQL (code below)
* `docker-compose run web pipenv run manage.py createsuperuser`
* `docker compose up`
  
PostgreSQL setup:
```code python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

```
 
More info:

https://akademiait.com.pl/