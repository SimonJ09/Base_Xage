#!/bin/bash
pip install --upgrade pip
python manage.py makemigrations
python manage.py migrate
gunicorn Xage1.wsgi:application --bind 0.0.0.0:$PORT --workers 4