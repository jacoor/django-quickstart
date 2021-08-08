#!/bin/bash
python manage.py collectstatic --noinput
ls -al /app/static/
ls -al /app/static/www
ls -al /app/static/www/css
python manage.py migrate
