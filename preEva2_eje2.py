# Ejercicio 2: Número primo
# Escribe una función llamada es_primo que determine si un número ingresado por el usuario
# es primo o no. Un número primo solo es divisible entre 1 y si mismo.

def es_primo(_numero):
    respuesta = True
    if (_numero == 2 or _numero == 3 or _numero == 5):
        respuesta = True
    else:
        if (_numero % 2 == 0):
            #si mi numero al dividirlo por 2, el resto es cero, es divisible por 2
            respuesta = False
        if (_numero % 3 == 0):
            respuesta = False
        if (_numero % 5 == 0):
            respuesta = False
    return respuesta

# Implementacion
numero = int(input("Ingrese un numero para saber si es primo: "))

print("El numero [",numero,"] es primo? : " , es_primo(numero))
