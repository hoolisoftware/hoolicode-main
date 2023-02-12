#! /bin/bash

python manage.py compilemessages -v 0
python manage.py makemigrations --no-input -v 0
python manage.py migrate -v 0 --no-input

exec python manage.py runserver 0.0.0.0:8000