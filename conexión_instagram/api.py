import json
import requests
import os
import time

def get_token():
    """Carga el token de acceso desde el archivo token.json."""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'token.json'), 'r') as f:
            return json.load(f)['token']
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'token.json'.")
        return None

def get_inbox_messages():
    """Obtiene los mensajes de la bandeja de entrada usando el token de acceso."""
    access_token = get_token()
    if not access_token:
        return None

    # URL base para la API de Instagram.
    # Necesitas reemplazar 'TU_ID_DE_PAGINA' con tu ID de página de Facebook.
    url = "https://graph.facebook.com/v19.0/TU_ID_DE_PAGINA/conversations"
    params = {
        "access_token": access_token,
        "fields": "messages{message,from,created_time}"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza un error para códigos de estado 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Instagram: {e}")
        return None

if __name__ == "__main__":
    messages = get_inbox_messages()
    if messages:
        print(json.dumps(messages, indent=4))
    else:
        print("No se pudieron obtener los mensajes.")
