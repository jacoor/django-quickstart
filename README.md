# django-quickstart

This is a simple django quickstart project, part of AkadamiaIT initiative.
Video tutorial: [Akademia IT Youtube](https://www.youtube.com/watch?v=7ZKccKcuF00)

## Quick and dirty start
* Create admin user: `docker-compose run web pipenv run manage.py createsuperuser`
* Start Django `docker compose up`

## Prereguisities:
* CLI knowledge
* Docker and docker compose

## If you follow the video - commands:
* `docker build .`
* `docker-compose run web pipenv run django-admin startproject quickstart .`
** initial start will fail because of missing django files but will create database directories
* `docker compose up`
** will fail because there is no project set up.
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

https://django.akademiait.com.pl/