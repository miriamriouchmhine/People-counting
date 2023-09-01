import telegram
#Crea una instancia del objeto 'Bot'
botAdmin = telegram.Bot(token= "TU_TOKEN")
#Función que envia el mensaje que se le envia
async def send_telegram_message(message):
    # Se utiliza el método send_message para enviar el mensaje que se le pasa como argumento,
    #  y utiliza el chat_id para saber a que canal enviarlo
	await botAdmin.send_message(chat_id = "TU_CHAT_ID", text = message)
	
async def main():
    await send_telegram_message("Esta es una alerta de prueba")

# Crea un bucle de eventos asyncio y ejecuta la función main()
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
