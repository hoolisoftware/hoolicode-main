#! /bin/bash

mkdir -p logs/
mkdir -p locale/

bash /wait-for-it.sh database:5432 --timeout=30 -- echo "Postgres is up"

exec "$@"
