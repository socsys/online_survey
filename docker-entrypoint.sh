#!/usr/bin/env bash

# Wait for the database service to be available
until nc -z -v -w30 ${DB_HOST} ${DB_PORT}; do
  echo "Waiting for the database service to be available..."
  sleep 1
done
echo "Connected to database."

python manage.py migrate --noinput
if [ $? -ne 0 ]; then
    echo "Migration failed." >&2
    exit 1
fi

# if arguments passed, execute them
# bring up an instance of project otherwise
if [[ $# -gt 0 ]]; then
    INPUT=$@
    sh -c "$INPUT"
else
    mkdir -p /var/log/online_survey

    if [ "$DEBUG" = "True" ]; then
        python manage.py collectstatic --noinput
    fi

    echo "Starting Gunicorn..."
    exec gunicorn online_survey:application \
        --config /app/gunicorn.conf.py \
        --reload
fi
