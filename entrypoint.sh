#!/bin/bash
set -e
source /env/bin/activate
# Exécuter les migrations Django au démarrage du conteneur
echo "Executing Django migrations..."
python manage.py migrate

echo "Executing Django collect staticfiles..."
python manage.py collectstatic  --noinput

# Lancer le serveur Django
echo "Starting Django server..."

python manage.py runserver 127.0.0.1:8000
