#Ejercicio 1: Validador de contraseña segura

# Crea una función llamada es_contrasena_segura que reciba una contraseña como parámetro
# la contraseña y verifique si cumple con los siguientes requisitos:

# [OK] Tiene al menos 8 caracteres
# Contiene al menos una letra mayúscula
# Contiene al menos una letra minúscula
# Contiene al menos un número
# Contiene al menos un simbolo

# Si cumple con todos los requisitos, la función debe retornar True, en caso contrario False.

def es_contrasena_segura(_password):
    respuesta = False
    #inicio: nuestro codigo de validacion va aqui
    
    # validamos el largo, ocupamos la funcion len / que significa length, que significa LARGO
    es_larga = len(_password) >= 8 # largo
    tiene_minuscula = any(c.islower() for c in _password) #minusculas
    tiene_mayuscula = any(c.isupper() for c in _password) #mayusculas
    tiene_numero = any(c.isdigit() for c in _password) #numeros
    tiene_simbolo = any(not c.isalnum() for c in _password) #simbolo

    respuesta = es_larga and tiene_minuscula and tiene_mayuscula and tiene_numero and tiene_simbolo

    #fin: nuestro codigo de validacion va aqui
    return respuesta

# Implementación del código
clave = input("Ingrese una contraseña segura (minimo 8 caracteres, 1 caracter minuscula, 1 mayuscula y 1 numero): ")
if (es_contrasena_segura(clave)):
    print("Buena! la contraseña es segura!")
else:
    print("Mala! debes crear una contraseña realmente segura (minimo 8 caracteres, 1 caracter minuscula, 1 mayuscula y 1 numero).")
