#!/usr/bin/sh
source /var/www/html/venv/bin/active
python /var/www/html/manage.py makemigrations
python /var/www/html/manage.py migrate