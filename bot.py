#Librería para crear un bot básico en python
import random

class Bot:

    def __init__(self,nombre):
        self.nombre = nombre
        self.preguntas = {}
        self.respuetaPredefinida = ""

    def establecer(self,preguntas,respuestas):
        
        for pregunta  in  preguntas:
            self.preguntas[pregunta.lower()] = respuestas
    
    def sinInformacion(self,respuesta ="Debes proporcionarme información para poderte ayudar"):
        self.respuetaPredefinida = respuesta

    
    def responder(self,pregunta):

        solicitud  = pregunta.lower()

        if solicitud in self.preguntas:

            respuestas  = self.preguntas[solicitud]

            respuesta = random.choice(respuestas)

            return respuesta
    
        else:

            return self.respuetaPredefinida

    def iniciar(self):
        return f"Hola mi nombre es {self.nombre}, estoy aquí para ayudarte."     

if __name__ == "__main__":
    bot = Bot("Jesús")
    bot.establecer(["Hola","buenos días","buenas tardes","buenas Noches","mucho gusto"],["Hola, ¿en que te puedo ayudar?","Bienvenido, estoy aquí para ayudarte","A sus ordenes", "Hola ,en que te puedo ayudar el día de hoy"])
    bot.establecer(["Necesito información","información de los productos","Me pueden compartir información de los productos"],["Claro, tenemos consolas, controles y accesorios de videojuegos","Tenemos variedad de productos relaciosnados con los videojuegos","Vendemos productos para jugar videojuegos y su mantenimeinto"])
    bot.establecer(["¿Donde estan ubicados?","¿Donde se ubican?","¿Donde esta su sucursal?","¿Donde esta su negocio?","¿Donde esta el establecimiento?","ubicación",],["Estamos en Privada ejemplo 123 Colonia ejemplo","Nos ubicamos en Privada ejemplo 123 Colonia ejemplo","Estamos en Privada ejemplo 123 Colonia ejemplo"])
    bot.establecer(["Gracias","Muchas gracias","Gracias por la información"],["De nada, es un placer ayudar","No hay de que","Estamos para servir"])

    bot.sinInformacion("No pude encontrar información con la que te puede ayudar")

    print(bot.iniciar())
    
    while True:

        print(bot.responder(input("Preguntar algo:")))