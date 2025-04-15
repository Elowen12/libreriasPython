#Libreria para colorear texto en consola
#Versión 1.0.0
#Licencia MIT

class Colores:
    def __init__(self):
        self.negro = "\033[30m"          # Negro
        self.rojo = "\033[31m"           # Rojo
        self.verde = "\033[32m"          # Verde
        self.amarillo = "\033[33m"       # Amarillo
        self.azul = "\033[34m"           # Azul
        self.magenta = "\033[35m"        # Magenta
        self.cian = "\033[36m"           # Cian
        self.blanco = "\033[37m"         # Blanco

class textoColoreado(Colores):

    def __init__(self):
         super().__init__()

    def colorear(self,texto:str,color:str):

        return f"{color}{texto}{self.blanco}"

if __name__ == "__main__":

    colorear = textoColoreado()

    print(colorear.colorear("Texto Coloreado",colorear.magenta))
    print(colorear.colorear("Texto Coloreado",colorear.cian))
    print(colorear.colorear("Texto Coloreado",colorear.amarillo))
    print(colorear.colorear("Texto Coloreado",colorear.verde))
    print(colorear.colorear("Texto Coloreado",colorear.rojo))
    
