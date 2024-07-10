#!/bin/bash

set -e

# Esecuzione delle migrazioni del DB
python manage.py makemigrations
python manage.py migrate

# Creazione del superutente
python manage.py shell < utils/create_superuser.py

# Avvia il server Django
exec "$@"