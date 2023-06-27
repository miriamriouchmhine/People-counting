import cv2

async def verificar_estado_camara(url):
    
    # Abrir el flujo de video
    cap = cv2.VideoCapture(url)

    # Comprobar si se están recibiendo fotogramas
    frames_recibidos = True if cap.read()[0] else False

    # Cerrar el flujo de video
    cap.release()

    return frames_recibidos


  