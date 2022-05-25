from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

from controllers import ctlEmpresas


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'baselogin'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def inicio():
    ctlEmpresas.ctlRegistroEmp()
    return render_template("views/inicio.html")

if __name__ == '__main__':
    app.secret_key = "kamata16angulo"
    app.run(debug=True)