#! /bin/bash

python manage.py migrate -v 0
python manage.py compilemessages -v 0
python manage.py ensure_admin --username admin --password admin

exec python manage.py runserver 0.0.0.0:8000
