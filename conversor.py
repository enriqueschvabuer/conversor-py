

def conversor (valor_dolar):
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    dolares = str(round(cantidad_moneda / valor_dolar, 2))
    print ("tienes $" + dolares + " dolares ")
    


def run():
    respuesta = "s"
    while respuesta == "s" :

        tipo_moneda = int(input("""
        Bienvenido al conversor de monedas multipais 

        1-Pesos Argentinos
        2-Pesos Chilenos
        3-Pesos Uruguayos

        Elige una opción: 

        """))

        if tipo_moneda == 1:  
            conversor (196)   
        elif tipo_moneda == 2:
            conversor (815) 
        elif tipo_moneda == 3:
            conversor (42)   
        else:
            print("Ingresaste una opción incorrecta")
        
        respuesta = input("desea continuar (s/n):")
        
        
        if respuesta == "n" :
            exit ()
        elif respuesta != "s":
            respuesta
            respuesta=input("Ingresaste una opcion incorrecta.desea continuar (s/n):")
         



if __name__ == "__main__":
    run()
