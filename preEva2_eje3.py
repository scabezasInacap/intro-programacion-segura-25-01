# Ejercicio 3: Adivina el número secreto
# Escribe un programa que elija un número aleatorio del 1 al 100
# y permita al usuario adivinarlo. El programa debe dar pistas si el número es mayor o menor,
# y contar cuántos intentos toma hasta acertar. Usa funciones y bucles.

import random #aleatorio

def jugar_numero_secreto(_numeroBuscado, _numeroSecreto):
    if (_numeroBuscado == _numeroSecreto):
        return True
    elif (_numeroBuscado < _numeroSecreto):
        print("Pista: Es mayor")
        return False
    elif (_numeroBuscado > _numeroSecreto):
        print("Pista: Es menor")
        return False
    else:
        return False

jugar = True

while (jugar):
    cantidadIntentos = 1
    numeroSecreto = random.randint(1, 50)
    # print("El nuevo numero secreto [" , numeroSecreto, "]")
    numero = int(input("Ingrese numero: "))
    while (cantidadIntentos < 4):
        #evaluamos
        respuesta = jugar_numero_secreto(numero, numeroSecreto)
        if (not respuesta):
            numero = int(input("Ingrese otro numero: "))
            cantidadIntentos += 1
        else:
            jugar = True
            print("Ganaste! en ", cantidadIntentos, " intentos")
            cantidadIntentos = 10
    if (cantidadIntentos == 4):
        print("No hay puntitos para ti! [",numeroSecreto,"]")
