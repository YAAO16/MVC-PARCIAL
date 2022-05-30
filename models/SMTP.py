from smtplib import SMTP
from email.message import EmailMessage

username = 'magdelinpai1999@gmail.com'
password = '1124867339'

def tokenConfirmacion(email):
    msg = EmailMessage()
    msg.set_content('Señor usuario bienvenido',)

    msg['Subject'] = 'confirmcion correo'
    msg['From'] = username
    msg['To'] = email


    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)

    server.quit()