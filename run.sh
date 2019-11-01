#!/bin/bash
pip install -r requirements.txt
python manage.py makemigrations app_models
python manage.py migrate app_models
python manage.py runserver 0.0.0.0:8000
