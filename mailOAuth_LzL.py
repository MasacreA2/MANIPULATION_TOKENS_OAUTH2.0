from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
from colorama import Fore, Style, init

# Inicialización de colorama
init(autoreset=True)
banner = f"""
{Fore.CYAN}=====================================================================
{Fore.MAGENTA}           
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣙⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠻⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡟⠹⠿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠋⡬⢿⣿⣷⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⢸⡇⢸⣿⣿⣿⠟⠁⢀⣬⢽⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣧⣈⣛⣿⣿⣿⡇⠀⠀⣾⠁⢀⢻⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣧⣄⣀⠙⠷⢋⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠸⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⢹⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠹⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠙⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
𝕍 𝕊  𝟙.𝟘
{Fore.YELLOW}𝕄 𝔸 𝕀 𝕃  𝕆 𝔸 𝕌 𝕋 ℍ  𝔾 𝕆 𝕆 𝔾 𝕃 𝔼 

{Fore.GREEN}𝔹𝕪 : 𝔸𝕝𝕖𝕩𝕚𝕤 𝕃𝕫𝕃 = 𝕄𝕒𝕤𝕒𝕔𝕣𝕖𝔸𝟚

{Fore.CYAN}==============================================================="""
print(banner)

# Client ID y Client Secret
CLIENT_ID = " TU CLIENTE ID DE LA APLICACION"
CLIENT_SECRET = "TU CLIENTE SECRETO DE  LA APLICACION"


# Función para refrescar el token de acceso usando el refresh token
def obtener_token_acceso(refresh_token):
    # Crea las credenciales usando el refresh token
    credentials = Credentials(
        None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    try:
        # Intenta refrescar el token de acceso
        credentials.refresh(Request())
        # Devuelve el nuevo token de acceso
        return credentials.token
    except RefreshError as e:
        # Maneja el error si no se puede refrescar el token
        print(Fore.RED + "Error al refrescar el token:")
        print(Fore.RED + str(e))
        return None



# Función para enviar un correo electrónico
def enviar_correo(access_token):
    # Construye el servicio de la API de Gmail
    service = build('gmail', 'v1', credentials=Credentials(token=access_token))

    # Obtiene la información del usuario autenticado
    usuario_autenticado = service.users().getProfile(userId='me').execute()
    remitente = usuario_autenticado['emailAddress']

    destinatario = input("Por favor ingrese el correo del destinatario: ")
    asunto = input("Por favor ingrese el asunto del correo: ")
    mensaje = input("Por favor ingrese el mensaje del correo: ")

    # Crea el mensaje de correo
    mensaje_mime = MIMEText(mensaje)
    mensaje_mime['to'] = destinatario
    mensaje_mime['subject'] = asunto
    mensaje_mime['from'] = remitente  # Utiliza la dirección de correo electrónico del usuario autenticado como remitente

    # Codifica el mensaje en base64
    raw = base64.urlsafe_b64encode(mensaje_mime.as_bytes()).decode()

    # Llama a la API para enviar el mensaje
    try:
        mensaje_enviado = service.users().messages().send(userId='me', body={'raw': raw}).execute()
        print(Fore.GREEN + "Mensaje enviado con ID:", mensaje_enviado['id'])
    except Exception as e:
        print(Fore.RED + "Error al enviar el mensaje:", e)



# Función para obtener los mensajes de Gmail
def obtener_mensajes(access_token):
    # Construye el servicio de la API de Gmail
    service = build('gmail', 'v1', credentials=Credentials(token=access_token))

    # Llama a la API para obtener los mensajes
    try:
        mensajes = service.users().messages().list(userId='me').execute()
        print(Fore.YELLOW + "Lista de mensajes:")
        for mensaje in mensajes['messages']:
            detalle_mensaje = service.users().messages().get(userId='me', id=mensaje['id']).execute()
            remitente = next((item['value'] for item in detalle_mensaje['payload']['headers'] if item['name'] == 'From'), None)
            asunto = next((item['value'] for item in detalle_mensaje['payload']['headers'] if item['name'] == 'Subject'), None)
            descripcion = detalle_mensaje.get('snippet', '')  # Descripción del mensaje, si está disponible

            # Verifica si el remitente y el asunto existen antes de imprimirlos
            if remitente and asunto:
                print(Fore.GREEN + f"Enviado por: {remitente}")
                print(Fore.CYAN + f"Asunto: {asunto}")
                print(Fore.WHITE + f"Descripción: {descripcion}")
                print()
            else:
                print(Fore.RED + "No se pudo obtener el remitente o el asunto del mensaje.")
    except Exception as e:
        print(Fore.RED + "Error al obtener los mensajes:", e)



# Solicitar detalles al usuario
opcion = input("Por favor seleccione una opción:\n1. Enviar correo electrónico\n2. Obtener mensajes de Gmail\n")

refresh_token = input("Por favor ingrese su refresh token: ")

# Obtener el nuevo token de acceso
token_acceso = obtener_token_acceso(refresh_token)

if token_acceso:
    print(Fore.GREEN + "Token de acceso actualizado:", token_acceso)

    if opcion == "1":
        enviar_correo(token_acceso)
    elif opcion == "2":
        obtener_mensajes(token_acceso)
    else:
        print(Fore.RED + "Opción inválida.")
else:
    print(Fore.RED + "No se pudo obtener el token de acceso.")
