import hashlib
from flask import session 

from db import db
from models import SMTP

mysql = db.conexion
mysql.autcommit = True

#from config import database
#mysql = database.mysql
def registroEmpresa(name,email,password,imagen,celular,direccion,descripcion):
    
    password = hashlib.sha1(password.encode()).hexdigest()
    
    cur = mysql.cursor()
    
    cur.execute("INSERT INTO users (name, email, password, imagen, celular, direccion, descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,email,password,imagen,celular,direccion,descripcion,))
        
   
    
    session['name'] = name
    session['email'] = email
    SMTP.tokenConfirmacion(email)
    return [True, 'Señor usuario bienvenido']

def mdlEntrarEmp(email,password):
    consulta = True
    cur = mysql.cursor()
    password = hashlib.sha1(password.encode()).hexdigest()
    
    """cur.execute("SELECT * FROM users WHERE email = %s and password=%s and estado='1'", (
            email,
            password,
            ))"""
    cur.execute("SELECT * FROM users WHERE email = %s and password=%s ", (
            email,
            password,
            ))
    
    usuario = cur.fetchone()
    cur.close()
    if usuario:
            if password == usuario["password"]:
                session['name']=usuario['name']
                session['email']=usuario['email']
                session['password']=usuario['password']
                fls =  ("Bienvenido")
                
            else:
                consulta = False
                
                fls =  ("correo o contraeña incorrectos")
                #return render_template("usuario o contraseña incorrectos")
                print("no entro el usuario")
    else:
        print("usuario no encontrado")
        consulta = False
        
        fls = ("alguno de los campos son incorretos")
    return [consulta,fls]

def recperarPASS(correo):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM usuarios WHERE correo = %s and estado='1'", (
                correo,
                ))
    
    usuario = cur.fetchone()
    cur.close()
    if not(usuario):
        print("no entro")
        return [False, 'correo invalido']
    
def conncet():
    cur = mysql.cursor()
    cur.execute("""
                    SELECT
                `id`,
                `descripcion`
                FROM
                `users`""")
    usuario = cur.fetchall()
    print(usuario)
    cur.close()
