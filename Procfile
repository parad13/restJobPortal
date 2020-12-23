release: python manage.py migrate 
    
web: gunicorn jobs.wsgi --log-file -
