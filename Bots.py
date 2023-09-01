import telegram
import asyncio
from mylib.alertas import verificar_estado_camara, verificar_ping_camara, obtener_ultimo_dato
from mylib.config import url, ip

#Cargar bot Admin

async def send_telegram_message(message):
	print("estoy en el send_message")
	botAdmin = telegram.Bot(token= "6201064848:AAEjSID8nnPto0uwqQgWsW0r0Sjue7tnqig")
	await botAdmin.send_message(chat_id = "-1001947006979", text = message)

#Cargar bot alumnos
async def send_telegram_message_Alumn(message):
	botAlumn = telegram.Bot(token= "6062087905:AAE3wffPdFFfxmP2wVaoZizT_l5lgZYOOUg")
	await botAlumn.send_message(chat_id = "-1001925970449", text = message)

connected = False
#MAIN 
async def main():
	
	
	global connected  # Declarar la variable global
	print("estoy en  main")

	while True:
		print("estoy en el while truee")
		ocupacion = obtener_ultimo_dato()
		if ocupacion is not None:
			mensaje_ocu = f"La ocupación es de {ocupacion}"
			await send_telegram_message(mensaje_ocu)
			await send_telegram_message_Alumn(mensaje_ocu)	
		# Obtener el estado de la cámara
		estado_camara = await verificar_estado_camara(url)
		estado_ping = await verificar_ping_camara(ip)
		if estado_ping and estado_camara and not connected:
			mensaje = "La cámara ya está conectada"
			await send_telegram_message(mensaje)
			connected = True
		elif (not estado_camara or not estado_ping) and connected:
			mensaje = "La cámara no esta conectada"
			await send_telegram_message(mensaje)
			connected = False
        
		# Esperar 30 minutos
		await asyncio.sleep(1800)

		
asyncio.run(main())