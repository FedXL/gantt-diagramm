
import os, sys
sys.path.insert(0, '/var/www/u1805305/data/www/gantt-diagramm.site/Gant')
sys.path.insert(1, '/var/www/u1805305/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Gant.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()