#!/bin/bash

# Esegui le migrazioni
python manage.py makemigrations
python manage.py migrate

# Avvia il server Django
python manage.py runserver 0.0.0.0:8000
