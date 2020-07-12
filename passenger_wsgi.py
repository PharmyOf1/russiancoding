import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/note_site')

INTERP = os.path.expanduser("~/russianandcoding.philharm.com/venv/russian/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/venv/russian/bin')
sys.path.insert(0,'$HOME/venv/russian/lib/python3.8/site-packages/django')
sys.path.insert(0,'$HOME/venv/russian/lib/python3.8/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "note_site.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

