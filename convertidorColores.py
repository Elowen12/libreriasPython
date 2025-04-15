#Libreria para convertir colores de rgb,rgba hexadecimal
#Versión 1.0.0
#Licencia MIT

class ConvertidorColores:

    def __init__(self):
        pass

    #Convertir RGB a hexadecimal
    def rgb_a_hex(self,r:int,g:int,b:int):

        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    #Convertir hexadecimal a RGB
    def hex_a_rgb(self,hex_color:str):

        color = hex_color[1:]

        r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
        return r, g, b
    

if __name__ == "__main__":
    convertidor = ConvertidorColores()
    print(convertidor.rgb_a_hex(55,25,0))
    
    r,g,b = convertidor.hex_a_rgb("#371900")
    print(f"{r},{g},{b}")
    