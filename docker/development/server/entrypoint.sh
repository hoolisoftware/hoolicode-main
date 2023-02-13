#! /bin/bash

set -o errexit
set -o pipefail
set -o nounset

mkdir -p logs/
mkdir -p locale/

bash /wait-for-it.sh database:5432 --timeout=30 -- echo "Postgres is up"

exec "$@"