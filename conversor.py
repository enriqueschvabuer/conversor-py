def conversor (valor_dolar):
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    dolares = str(round(cantidad_moneda / valor_dolar, 2))
    print ("tienes $" + dolares + " dolares ")

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
    print("Escribiste una opción incorrecta")
    exit()



