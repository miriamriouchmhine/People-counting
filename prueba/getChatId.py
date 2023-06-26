#Importamos la libreria de telegram que necesitamos
import telegram

#Cargamos el token 
bot_token = "6062087905:AAE3wffPdFFfxmP2wVaoZizT_l5lgZYOOUg"
bot = telegram.Bot(token=bot_token)

#Función que obtiene el chat_id. 
async def obtener_chat_id():
    #Nombre de nuestro canal
    username = "@biblioAlumnosUPCT"
    # Hay que utilizar la palabra clave 'await' para esperar la finalización 
    # del método get_chat() y obtener el objeto chat completo. 
    # Si no utilizamos esto saltará un error ya que intentara acceder al 
    # atributo 'id' de un objeto coroutine en lugar de esperar a obtener 
    # el resultado correcto.
    response = await bot.get_chat(username)
    chat_id = response.id
    return chat_id

async def main():
    chat_id = await obtener_chat_id()
    print(chat_id)


# Crea un bucle de eventos asyncio y ejecuta la función main()
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())