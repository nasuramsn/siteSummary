sleep 5
uwsgi --ini /app/app/uwsgi.ini
sleep 5
uwsgi --socket :8001 --wsgi-file /app/app/sitesummary/wsgi.py