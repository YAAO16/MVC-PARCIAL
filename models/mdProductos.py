#from app import mysql
from flask import session 

from db import db 

mysql = db.conexion



def creaProd():
    name= session['name']
    email= session['email']
    cur = mysql.cursor()
    cur.execute("SELECT `id` FROM `users` WHERE users.`name`=%s AND  users.`email`=%s;",
                (name,email))
    usuario = cur.fetchone()
    print(usuario)
    cur.close()