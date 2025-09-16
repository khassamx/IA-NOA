import time
from conexión_instagram.api import get_inbox_messages
from datos_bot_noa.logs import log_message

# Aquí importaremos la función que procesará los mensajes
from datos_bot_noa.reconocimiento_chats import procesar_mensaje

def escuchar_mensajes():
    """Bucle principal para que Noa escuche y procese mensajes."""
    log_message("Noa se está conectando a Instagram...", "INFO")
    
    # Intenta obtener mensajes. La función ya maneja la conexión con el token.
    mensajes_recibidos = get_inbox_messages()

    if mensajes_recibidos:
        log_message("Conexión exitosa. Noa está escuchando mensajes nuevos.", "INFO")
        log_message("Mostrando los últimos mensajes de la bandeja de entrada:", "INFO")
        
        # Aquí puedes iterar sobre los mensajes para procesarlos
        if 'data' in mensajes_recibidos:
            for conversacion in mensajes_recibidos['data']:
                for mensaje in conversacion['messages']['data']:
                    texto_mensaje = mensaje['message']
                    remitente = mensaje['from']['username'] # Requiere los permisos correctos
                    
                    log_message(f"Mensaje de {remitente}: {texto_mensaje}", "CHAT")
                    
                    # Procesa el mensaje con la lógica de Noa
                    respuesta_noa = procesar_mensaje(texto_mensaje)
                    log_message(f"Respuesta de Noa a {remitente}: {respuesta_noa}", "CHAT")
                    
                    # NOTA: La función para enviar mensajes se agregará más tarde.
    else:
        log_message("No se pudo establecer la conexión o no hay mensajes nuevos.", "WARNING")

def iniciar_bot():
    """Función para ejecutar el bot de forma continua."""
    log_message("Iniciando Noa, tu IA amiga de Instagram.", "INFO")
    
    # Bucle infinito para escuchar mensajes constantemente
    while True:
        escuchar_mensajes()
        log_message("Esperando 60 segundos antes de buscar nuevos mensajes...", "INFO")
        time.sleep(60)

if __name__ == "__main__":
    iniciar_bot()
