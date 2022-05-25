#from app import app, mysql
from config import database
mysql = database.mysql
def registroEmpresa():
    cur = mysql.connection.cursor()
    cur.execute("""
                    SELECT
                `id`,
                `descripcion`
                FROM
                `users`""")
    usuario = cur.fetchall()
    print(usuario)
    cur.close()
    