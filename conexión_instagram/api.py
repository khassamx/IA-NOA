import instaloader
import getpass
import os

def login_instagram():
    """
    Inicia sesión en Instagram, pidiendo el usuario y la contraseña.
    """
    try:
        L = instaloader.Instaloader()
        
        # Pide el nombre de usuario
        usuario = input("Nombre: ")
        
        # Pide la contraseña de forma segura para que no se vea en pantalla
        contraseña = getpass.getpass("Contraseña: ")

        print("Iniciando sesión...")
        L.login(usuario, contraseña)
        print("¡Sesión iniciada exitosamente!")
        
        return L

    except instaloader.exceptions.BadCredentialsException:
        print("Error: El nombre de usuario o la contraseña son incorrectos.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al iniciar sesión: {e}")
        return None
