#!/bin/bash
python manage.py collectstatic --noinput
ls -al /app/static/
ls -al /app/static/www
python manage.py migrate
