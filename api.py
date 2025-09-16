import instaloader
import json
import os

# Cargar las credenciales desde el archivo JSON
# La ruta de este archivo es relativa a donde ejecutes el script
# Si el script principal está en la carpeta raíz (NoaIA_Instagram), la ruta será:
# 'conexión_instagram/config_credenciales.json'
def get_credentials():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'config_credenciales.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'config_credenciales.json'.")
        return None

# Función para iniciar sesión en Instagram
def login_instagram():
    credentials = get_credentials()
    if not credentials:
        return None

    L = instaloader.Instaloader()

    try:
        print("Iniciando sesión en Instagram...")
        L.load_session_from_file(credentials['usuario'])
        print("Sesión cargada exitosamente.")
    except FileNotFoundError:
        try:
            L.login(credentials['usuario'], credentials['contraseña'])
            L.save_session_to_file(credentials['usuario'])
            print("Sesión iniciada y guardada.")
        except instaloader.exceptions.BadCredentialsException:
            print("Error: Credenciales de Instagram incorrectas.")
            return None
        except Exception as e:
            print(f"Ocurrió un error al iniciar sesión: {e}")
            return None
    return L

# Función de prueba para verificar que la conexión funciona
def check_connection():
    L = login_instagram()
    if L:
        print("\n¡Conexión exitosa a Instagram!")
        return L
    else:
        print("\nNo se pudo establecer la conexión.")
        return None

if __name__ == "__main__":
    check_connection()
