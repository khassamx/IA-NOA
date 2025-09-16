import time
from conexión_instagram.api import login_instagram
from datos_bot_noa.logs import log_message

def mostrar_bienvenida():
    """Muestra el arte ASCII y el mensaje de bienvenida."""
    print("""
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔═══╝ ██╔══██║██║╚██╔╝██║
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║     ██║  ██║██║ ╚═╝ ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
""")

def iniciar_bot():
    """Función para ejecutar el bot de forma continua."""
    mostrar_bienvenida()
    log_message("¡Hola! Soy Noa. Para empezar, necesito que inicies sesión en Instagram.", "INFO")
    
    L = login_instagram()
    if not L:
        return  # Detiene el programa si el login falla

    log_message("Conexión exitosa. Noa está escuchando mensajes nuevos.", "INFO")

    while True:
        # Aquí irá el código para leer y responder a los mensajes
        log_message("Esperando 60 segundos antes de buscar nuevos mensajes...", "INFO")
        time.sleep(60)

if __name__ == "__main__":
    iniciar_bot()
