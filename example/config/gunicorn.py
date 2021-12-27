import os

command = '/usr/bin/gunicorn'

# Configurable settings
worker_tmp_dir = os.getenv('GUNICORN_WORKER_TMP_DIR', None)
bind = '0.0.0.0:%s' % int(os.getenv('PORT', default='8000'))
workers = int(os.getenv('GUNICORN_WORKERS', default='3'))
loglevel = 'debug' if os.getenv('DEBUG', default='True').lower() in ['true', '1'] else 'info'

# Send logging to the console
errorlog = os.getenv('GUNICORN_ERROR_LOG', default='-')
accesslog = os.getenv('GUNICORN_ACCESS_LOG', default='-')
capture_output = errorlog != '-' or accesslog != '-'