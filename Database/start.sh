#!/bin/bash
pip install --upgrade pip
pip install pandas
pip install gunicorn
python manage.py makemigrations
python manage.py migrate
gunicorn Xage1.wsgi:application --bind 0.0.0.0:$PORT --workers 4