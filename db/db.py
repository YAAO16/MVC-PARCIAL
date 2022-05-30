import mysql.connector

conexion = mysql.connector.connect(
    
    host="localhost",
    user="adrian",
    password="",
    database="baselogin",
    port=3306,
    
)
   
conexion.autcommit = True

