#!/bin/bash

pip install -r requirements.txt
pip freeze

python manage.py makemigrations app
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
