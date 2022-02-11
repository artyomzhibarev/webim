#!/bin/sh


# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Run number generator
python manage.py num_gen

exec "$@"