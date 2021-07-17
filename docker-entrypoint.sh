#!/bin/bash
echo "Install packages"
pipenv install --dev

source /www/.venv/bin/activate
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting dev server"
python manage.py runserver 0.0.0.0:8000
