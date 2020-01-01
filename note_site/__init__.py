#This was a lifesafer on mac and rio
import pymysql, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mac-materials.settings")
pymysql.install_as_MySQLdb()
