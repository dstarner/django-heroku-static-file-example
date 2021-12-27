web: gunicorn -c example/config/gunicorn.py example.config.wsgi:application

# SPECIAL
# Release phase is responsible for migrating the database
release: ./scripts/release.sh