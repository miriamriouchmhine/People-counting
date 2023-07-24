import cv2
import ping3
import mysql.connector
from mylib.config import db_config

async def verificar_estado_camara(url):
    
    # Abrir el flujo de video
    cap = cv2.VideoCapture(url)

    # Comprobar si se están recibiendo fotogramas
    frames_recibidos = True if cap.read()[0] else False

    # Cerrar el flujo de video
    cap.release()

    return frames_recibidos

async def verificar_ping_camara(ip):
    # Realizar un ping a la cámara
    response = ping3.ping(ip)
    if response is not None:
        return True
    else: 
        return False


def obtener_ultimo_dato():
    try:
        #Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        #Consulta para obtener el último dato insertado 
        query = "SELECT fecha_hora, ocupacion FROM biblioteca ORDER BY fecha_hora DESC LIMIT 1"

        #Ejecutar la consulta 
        cursor.execute(query)

        #Obtener el resultado
        result = cursor.fetchone()
        if result:
            #El ultimo dato insertado se encuentra en result[0]
            return result[1]
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al obtener el ultimo dato de la base de datos:", err)
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


