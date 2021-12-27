#!/bin/bash
set -e

./manage.py collectstatic --no-input

./manage.py migrate

./manage.py createsuperuser --no-input --email test@example.com --username test || true