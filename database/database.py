from flask import Flask
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cartavirtual'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
print('This config the database or domain')