#python 3.5
import telebot 
bot = telebot.TeleBot("API_KEY")

def leeMensaje(mensajes):
    for mensaje in mensajes: #Este for each recorre cada mensaje dentro de la estructura que obtiene el bot de Telegram
        id_chat = mensaje.chat.id #Se necesita obtener el id del mensaje para saber a quien responder
        #Aqui se pueden hacer muchas cosas como por ejemplo saludar...
        #bot.send_message(id_chat, 'Hola soy un Bot mu guapo') 

bot.set_update_listener(leeMensaje) #Asigna la función correspondiente como listener

@bot.message_handler(commands=['ayuda'])
def ayudar(mensaje):
     id_chat= mensaje.chat.id #El id del chat para saber el destino de la respuesta que va a enviar el bot
     bot.send_message( id_chat, ':') 
     bot.send_message( id_chat, '/ayuda       -Muestra los comandos disponibles del bot.') 
     bot.send_message( id_chat, '/spam        -Envia un numero masivo de mensajes.') 

@bot.message_handler(commands=['spam'])
def spam(mensaje):
     numeroDeMensajesdelSpam = 100
     id_chat= mensaje.chat.id #El id del chat para saber el destino de la respuesta que va a enviar el bot
     for i in range(numeroDeMensajesdelSpam):
     	 bot.send_message( id_chat, '%d - SPAM' %(i)) 
    


bot.polling(none_stop=True)
