tipo_moneda = int(input("""
Bienvenido al conversor de monedas multipais

1-Pesos Argentinos
2-Pesos Chilenos
3-Pesos Uruguayos

Elige una opción: 

"""))


if tipo_moneda == 1:
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    valor_dolar = 196
    
elif tipo_moneda == 2:
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    valor_dolar = 815

elif tipo_moneda == 3:
    cantidad_moneda = float(input("ingrese cantidad de pesos: "))
    valor_dolar = 42
    
else:
    print("Escribe una opción correcta: ")


dolares = str(round(cantidad_moneda / valor_dolar, 2))
print ("tienes $" + dolares + " dolares ")