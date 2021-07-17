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
* `docker-compose run web pipenv run manage.py startapp www` - starts our website project as top level module.
  
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

## Styles
To generate css use 
```code shell
    foundation watch
```
in `www/static/www` directory. Important is it needs node 10 and will fail with newer version.
Now, this actually only needs to be run once, to generate required CSS and js files - other can be created manually, or, using scss if that is desired.

 
More info:

https://akademiait.com.pl/