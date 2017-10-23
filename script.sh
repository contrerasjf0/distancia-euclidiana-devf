#!/usr/bin/env bash
python manage.py migrate calculationEuclidiana zero
python manage.py migrate movies zero
python manage.py makemigrations
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 distanciaEuclidiana.wsgi:application
