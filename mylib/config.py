#===============================================================================
#""" Optional features config. """
#===============================================================================
import datetime

# Enter the ip camera url (e.g., url = 'http://191.138.0.100:8040/video')
url = "rtsp://biblioteca:camaraBibAlex@192.168.102.120:554/h264/ch1/main/av_stream"
ip = "192.168.102.120"
# ON/OFF for mail feature. Enter True to turn on the email alert feature.
ALERT = False
# Set max. people inside limit. Optimise number below: 10, 50, 100, etc.
# Threshold = 10
# Threading ON/OFF
Thread = False
# Auto run/Schedule the software to run at your desired time
Scheduler = True
# Auto stop the software after certain a time/hours
Timer = False

#Variables de configuración

#Definir las variables de la línea
line_color = (0, 0, 0)  #Color de la línea en formato BGR
line_thickness = 3      #Grosor de la línea en píxeles
line_position = 120   #Posición verticall de la línea

#Definir las variables del recorte de la imagen: pixel_start= en que pixel 
# comienza la imagen y pixel_end= a donde termina la imagen
pixel_start_height = 70
pixel_start_width = 50
pixel_end_height = 700
pixel_end_width = 600

#Tamaño máximo de nuestra frame en pixels
frame_size = 700

# Dirección entrada y salida
downIsEntry = False
#Argumentos
prototxt = "mobilenet_ssd/MobileNetSSD_deploy.prototxt"
model = "mobilenet_ssd/MobileNetSSD_deploy.caffemodel"

confidence_config = 0.4
skip_frames = 20

media = 115

#===============================================================================
# Variables de conexión a la base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "db"  
}

  # Por ejemplo, de lunes a viernes

# Verificar si la hora actual está dentro de la franja horaria de 8:30 a 21:00
def esta_dentro_de_franja_horaria():
    dias_permitidos = [0, 1, 2, 3, 4]
    ahora = datetime.datetime.now()
    # Verificar si el día de la semana está dentro de los días permitidos
    if ahora.weekday() not in dias_permitidos:
        return False
    
    hora_inicio = ahora.replace(hour=6, minute=0, second=0, microsecond=0)
    hora_fin = ahora.replace(hour=18, minute=58, second=0, microsecond=0)
    return hora_inicio <= ahora <= hora_fin