#!/bin/bash
set -e

# Source secrets
cp /etc/secrets-volume/env /code/mozillians/.env

if [ -e /code/mozillians/.env ]
then
  set -a && source /code/mozillians/.env && set +a
fi

# Initialize the pod
case "$1" in
  "celery")
    /code/bin/run-celery.sh ;;
  "celery-beat")
    /code/bin/run-celery-beat.sh ;;
  "run-prod")
    # Run bootstrap script contents
    python manage.py collectstatic --noinput
    python manage.py compress --force --engine jinja2 --extension=.html

    # Run production environment
    python manage.py migrate --noinput
    gunicorn mozillians.wsgi:application -w 2 -b 0.0.0.0:${PORT:-8000} --log-file -
    ;;
  *)
    echo "Provide a valid argument: celery, celery-beat or run-prod" ;;
esac
