import requests
from colorama import Fore, Style, init
# Validador de  tokens  Oauth 2.0  para aplicaciones de Googl3

init(autoreset=True)


banner = f"""
{Fore.CYAN}=================================================================================================================
{Fore.MAGENTA}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠉⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⡀⠀⠄⡀⠀⠀⠀⢀⣻⠀⠀⠀⣿⣿⣿⠿⠛⢉⣠⣉⠛⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠛⠉⠀⣾⡷⠂⢤⣍⠛⠿⣿⣿⣿⠿⢿⣿⣷⣧⡂⠀⠀⢠⣆⣴⣷⠿⠀⠀⠀⠛⠋⣡⣶⡆⠀⠙⣿⠀⠀⢨⡙⠻⢿⣿⣿
⣿⡿⠛⠁⠰⡆⠀⢠⣿⠀⠀⣸⡿⠁⠰⣶⡶⠂⢠⡈⠛⠉⠀⠀⠀⠀⠀⠈⠙⠋⣠⠂⠀⢠⣿⠀⠀⢻⣷⡀⠀⣿⣦⡀⠈⡇⠀⠠⣍⠛
⠋⢡⡄⠀⢀⠁⣠⣾⣿⠀⣰⣿⡇⠀⢀⣿⡇⠀⠸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⢸⣿⡄⠀⢸⣿⣷⡀⣿⣿⣷⣄⢣⡀⠀⠟⠀
⠀⢸⠀⣰⣿⣾⣿⣿⣿⣰⣿⣿⡇⢀⣾⣿⡇⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⠀⢸⣿⣿⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣸⣄
⣴⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⣿⣿⡇⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣆⣾⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠹⢿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⢿⠿⠷⠄⠛⢿⡿⠟⠁⠀⠀⢀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⠀⠀⠀⠉⠻⢿⡿⠋⠰⠿⠿⠟⠘⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⣦⣤⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿

.d88b.    db    8    8 88888 8   8 d88b   .d88b.    .d88b 8   8 8888 .d88b 8  dP    8    8888P 8    
8P  Y8   dPYb   8    8   8   8www8 " dP   8P  Y8    8P    8www8 8www 8P    8wdP     8      dP  8    
8b  d8  dPwwYb  8b..d8   8   8   8  dP    8b  d8    8b    8   8 8    8b    88Yb     8     dP   8    
`Y88P' dP    Yb `Y88P'   8   8   8 d888 w `Y88P'    `Y88P 8   8 8888 `Y88P 8  Yb    8888 d8888 8888 
                                                                                                        
                                                                                                            
{Fore.GREEN}𝔹𝕪 : 𝔸𝕝𝕖𝕩𝕚𝕤 𝕃𝕫𝕃 = 𝕄𝕒𝕤𝕒𝕔𝕣𝕖𝔸𝟚
{Fore.CYAN}===================================================================================================================
"""
print(banner)


# Obtener la dirección IP del usuario
ip_response = requests.get('https://httpbin.org/ip')
ip_data = ip_response.json()
user_ip = ip_data.get('origin', 'N/A')

# Solicitar el token al usuario
access_token = input("Por favor ingrese su token de acceso: ")

# URL de la API para obtener información del usuario
api_url = "https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,photos,locales,phoneNumbers,birthdays"

# Encabezados de la solicitud
headers = {
    "Authorization": f"Bearer {access_token}",
}

# Realizar la solicitud para obtener información del usuario
response = requests.get(api_url, headers=headers)

# Manejar la respuesta
if response.status_code == 200:
    user_info = response.json()
    print(Fore.GREEN + Style.BRIGHT + "Información del usuario:")
    print(Fore.YELLOW + f"Usuario: {user_info.get('names', [{}])[0].get('displayName', 'N/A')}")
    print(Fore.YELLOW + f"Nombre: {user_info.get('names', [{}])[0].get('givenName', 'N/A')}")
    print(Fore.YELLOW + f"Apellido: {user_info.get('names', [{}])[0].get('familyName', 'N/A')}")
    print(Fore.YELLOW + f"Email: {user_info.get('emailAddresses', [{}])[0].get('value', 'N/A')}")
    print(Fore.YELLOW + f"Fecha de nacimiento: {user_info.get('birthdays', [{}])[0].get('date', 'N/A')}")
    print(Fore.YELLOW + f"Imagen: {user_info.get('photos', [{}])[0].get('url', 'N/A')}")
    print(Fore.GREEN + Style.BRIGHT + "Información de la dirección IP:")
    print(Fore.YELLOW + f"Dirección IP: {user_ip}")
    
    # Obtener información del país asociado a la dirección IP
    ipinfo_response = requests.get(f"https://ipinfo.io/{user_ip}/json")
    if ipinfo_response.status_code == 200:
        ipinfo_data = ipinfo_response.json()
        country = ipinfo_data.get('country', 'N/A')
        latitude = ipinfo_data.get('loc', 'N/A').split(',')[0]
        longitude = ipinfo_data.get('loc', 'N/A').split(',')[1]
        print(Fore.YELLOW + f"País de la dirección IP: {country}")
        print(Fore.YELLOW + f"Latitud: {latitude}")
        print(Fore.YELLOW + f"Longitud: {longitude}")
    else:
        print(Fore.RED + "No se pudo obtener información del país.")
else:
    print(Fore.RED + Style.BRIGHT + f"No se pudo obtener la información del usuario: {response.status_code}, {response.text}")