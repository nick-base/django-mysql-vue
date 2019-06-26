#!/bin/bash

source activate demoweb
cd web
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
