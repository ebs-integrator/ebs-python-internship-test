#!/bin/bash

python manage.py collectstatic --noinput

if [ -z "$MANAGE_COMMAND" ]; then
  if [ "$MANAGE_PY" = "True" ]; then
    echo "Start manage.py"
    python manage.py runserver "${GUNICORN_BIND}" --noreload
  else
    echo "Start GUNICORN"
    python manage.py migrate
    gunicorn --workers="${GUNICORN_WORKERS}" --threads="${GUNICORN_THREADS}" --env DJANGO_SETTINGS_MODULE=config.settings config.wsgi:application -b "${GUNICORN_BIND}" --log-level info --timeout "${GUNICORN_TIMEOUT}"
  fi
else
  echo "Start $MANAGE_COMMAND command"
  python manage.py "${MANAGE_COMMAND}"
fi
