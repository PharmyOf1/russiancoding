import pymysql, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "code_blog.settings")
pymysql.install_as_MySQLdb()
