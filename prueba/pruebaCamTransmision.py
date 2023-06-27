import cv2
import time
# Lista de direcciones URL de las cámaras
camera_urls = [
    "rtsp://tapo2912:Riouch2000@192.168.1.9:554/h264/ch1/main/av_stream",
    #"rtsp://biblioteca:camaraBibAlex@192.168.102.120:554/h264/ch1/main/av_stream"
    #  Agregue más direcciones URL aquí si desea visualizar más cámaras
]

# Lista para almacenar las conexiones con las cámaras
caps = []
received_frames = 0
start_time = time.time()

capture_times = []
display_times = []
# Inicializa las conexiones con las cámaras
for url in camera_urls:
    cap = cv2.VideoCapture(url)
    caps.append(cap)

# Verifica si se pudieron inicializar todas las conexiones
for i, cap in enumerate(caps):
    if not cap.isOpened():
        print(f"No se puede conectar a la cámara {i + 1}")
        exit()

# Lee el primer frame de video de cada cámara
frames = []
for i, cap in enumerate(caps):
    ret, frame = cap.read()
    frames.append(frame)

    # Verifica si se pudo leer el primer frame
    if not ret:
        print(f"No se pudo leer el primer frame de la cámara {i + 1}")
        exit()

# Configura las dimensiones de las ventanas
widths = [int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) for cap in caps]
heights = [int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) for cap in caps]

# Crea ventanas para mostrar el video de cada cámara
window_names = [f"Cámara {i + 1}" for i in range(len(camera_urls))]
for i, name in enumerate(window_names):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, widths[i], heights[i])

# Mientras haya frames disponibles en el video de todas las cámaras
while all([cap.isOpened() for cap in caps]):
    # Lee el siguiente frame de cada cámara
    frames = []
    for i, cap in enumerate(caps):
        ret, frame = cap.read()
        frames.append(frame)

        # Verifica si se pudo leer el siguiente frame
        if not ret:
            break
        received_frames += 1
        capture_time = time.time()  # Tiempo de captura
        capture_times.append(capture_time)
        display_time = time.time()  # Tiempo de visualización (antes de la llamada imshow)
        display_times.append(display_time)
        cv2.imshow(window_names[i], frame)
    # Muestra el frame en la ventana correspondiente a cada cámara
    for i, frame in enumerate(frames):
        cv2.imshow(window_names[i], frame)

    # Verifica si se presionó la tecla "q" para detener la ejecución
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
end_time = time.time()
elapsed_time = end_time - start_time
fps = received_frames / elapsed_time
total_duration = elapsed_time  # Duración total en segundos, ajusta según tus necesidades
expected_frames = int(fps * total_duration)
latency = sum(display_times) - sum(capture_times)
average_jitter = sum(abs(display_times[i] - capture_times[i]) for i in range(len(capture_times))) / len(capture_times)

print("Número de frames recibidos:", received_frames)
print("Duración total (segundos):", elapsed_time)
print("Número de frames esperados:", expected_frames)
print("Latencia (segundos):", latency)
print("Jitter promedio (segundos):", average_jitter)

for cap in caps:
    cap.release()
cv2.destroyAllWindows()
