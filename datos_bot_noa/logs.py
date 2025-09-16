from datetime import datetime

def log_message(message, log_type="INFO"):
    """
    Función para registrar mensajes en la consola con marca de tiempo y tipo.
    Tipos de log: INFO, ERROR, DEBUG, WARNING.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{log_type}] {message}")

# Ejemplo de uso:
# log_message("El bot está escuchando nuevos mensajes.", "INFO")
# log_message("Hubo un error en la conexión.", "ERROR")
