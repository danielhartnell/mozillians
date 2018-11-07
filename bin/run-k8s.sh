#!/bin/bash

# Source secrets
cp /etc/secrets-volume/env /code/mozillians/.env

if [ -e /code/mozillians/.env ]
then
    set -a && source /code/mozillians/.env && set +a
fi

# Bootstrap container
python manage.py collectstatic --noinput
python manage.py compress --force --engine jinja2 --extension=.html

# Run prod environment
python manage.py migrate --noinput
gunicorn mozillians.wsgi:application -w 2 -b 0.0.0.0:${PORT:-8000} --log-file -
