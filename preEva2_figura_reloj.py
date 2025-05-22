# * * * *
#  * * *
#   * *
#    *
#   * *
#  * * *
# * * * *

# dado un numero 4, se muestra una figura como un reloj de arena

def fx_figura(_num, _car):
    # print(f"num: {_num} | car: {_car}")
    caracter = _car + ' '
    for i in range (0, _num):
        print(f"{' ' * i}{caracter * (_num - i)}")
    # segunda parte de la figura
    for j in range (2, (_num + 1)):
        print(f"{' ' * (_num - j)}{caracter * j}")




# app: que llama a la funcion y solicita el numero y el caracter

# paso 1: solicitar caracter
caracter = input("Ingrese un caracter para representar la firgura: ")

# Forma 1:

# paso 2: solicitar numero
# numero = int(input("Ingrese un numero para definir la figura: "))
# paso 3: validar que sea mayor que 2, sino, vuleve a pedirlo infinitas veces
#while numero < 2:
#    numero = int(input("Error: Ingrese un numero para definir la figura (mayor que 2): "))

# Forma 2:
while True:
    # paso 2: solicitar numero
    numero = int(input("Ingrese un numero para definir la figura: "))
    # paso 3: validar que sea mayor que 2, sino, vuleve a pedirlo infinitas veces
    if (numero >= 2):
        # se termina
        break
    else:
        print("Error: Ingrese un numero para definir la figura (mayor que 2): ")

print(f"numero: {numero} | caracter: {caracter}")

fx_figura(numero, caracter)
