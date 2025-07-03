import copy
#Ejercicio 1: Registro de Estudiantes
#Descripción: Crea un sistema sencillo para registrar estudiantes y sus calificaciones, permitiendo actualizar información.
#Instrucciones:
#Crea una lista vacía llamada registro_estudiantes.
#Define una función mostrar_registro(registro) que imprima todos los estudiantes y sus datos de forma legible.
#Agrega los siguientes estudiantes (diccionarios) a la lista registro_estudiantes en este orden:
#{"nombre": "Ana", "edad": 20, "calificaciones": {"Matematicas": 85, "Historia": 90}}
#{"nombre": "Pedro", "edad": 22, "calificaciones": {"Matematicas": 78, "Historia": 88}}
#{"nombre": "Luisa", "edad": 21, "calificaciones": {"Matematicas": 92, "Historia": 75}}
#Imprime el registro completo de estudiantes después de cada adición.
#Crea una función actualizar_calificacion(registro, nombre_estudiante, materia, nueva_nota) que actualice la calificación de un estudiante. La función debe utilizar deepcopy() para crear una copia del registro antes de la modificación y retornar True si el cambio se realizó correctamente (comparando la copia original con la modificada), False en caso contrario.
#Actualiza la calificación de "Ana" en "Matematicas" a 95 usando la función actualizar_calificacion. Muestra si el cambio fue exitoso.
#Imprime el registro final de estudiantes.
#Salida Esperada:
#--- Registro de Estudiantes ---
#No hay estudiantes registrados.
#--- Registro de Estudiantes ---
#Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 85, 'Historia': 90}
#--- Registro de Estudiantes ---
#Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 85, 'Historia': 90}
#Nombre: Pedro, Edad: 22, Calificaciones: {'Matematicas': 78, 'Historia': 88}
#--- Registro de Estudiantes ---
#Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 85, 'Historia': 90}
#Nombre: Pedro, Edad: 22, Calificaciones: {'Matematicas': 78, 'Historia': 88}
#Nombre: Luisa, Edad: 21, Calificaciones: {'Matematicas': 92, 'Historia': 75}
#Se actualizó la calificación de Ana en Matematicas?: True
#--- Registro de Estudiantes ---
#Nombre: Ana, Edad: 20, Calificaciones: {'Matematicas': 95, 'Historia': 90}
#Nombre: Pedro, Edad: 22, Calificaciones: {'Matematicas': 78, 'Historia': 88}
#Nombre: Luisa, Edad: 21, Calificaciones: {'Matematicas': 92, 'Historia': 75}

#Define una función mostrar_registro(registro) que imprima todos los estudiantes y sus datos de forma legible.
def mostrar_registro(registro):
    print("--- Registro de Estudiantes ---")
    if (len(registro_estudiantes) == 0):
        print("No hay estudiantes registrados.")
    else:
        for estudiante in registro:
            #print(estudiante)
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificaciones: {estudiante['calificaciones']}")

#Crea una función actualizar_calificacion(registro, nombre_estudiante, materia, nueva_nota) 
# que actualice la calificación de un estudiante. 
# La función debe utilizar deepcopy() para crear una copia del registro antes de la
#  modificación y retornar True si el cambio se realizó correctamente 
# (comparando la copia original con la modificada), False en caso contrario.

def actualizar_calificacion(registro, nombre_estudiante, materia, nueva_nota):
    #hayCambio = False
    registroNuevo = copy.deepcopy(registro)
    for estudiante in registroNuevo:
        if (estudiante['nombre'] == nombre_estudiante):
            estudiante['calificaciones'][materia] = nueva_nota
    #        hayCambio = True
            break
    #return hayCambio
    return registroNuevo

#Crea una lista vacía llamada registro_estudiantes.
registro_estudiantes = []
mostrar_registro(registro_estudiantes)
#Agrega los siguientes estudiantes (diccionarios) a la lista registro_estudiantes en este orden:
dic = {"nombre": "Ana", "edad": 20, "calificaciones": {"Matematicas": 85, "Historia": 90}}
registro_estudiantes.append(dic)
mostrar_registro(registro_estudiantes)
dic = {"nombre": "Pedro", "edad": 22, "calificaciones": {"Matematicas": 78, "Historia": 88}}
registro_estudiantes.append(dic)
mostrar_registro(registro_estudiantes)
dic = {"nombre": "Luisa", "edad": 21, "calificaciones": {"Matematicas": 92, "Historia": 75}}
registro_estudiantes.append(dic)
mostrar_registro(registro_estudiantes)
#Crea una función actualizar_calificacion(registro, nombre_estudiante, materia, nueva_nota) que actualice la calificación de un estudiante. La función debe utilizar deepcopy() para crear una copia del registro antes de la modificación y retornar True si el cambio se realizó correctamente (comparando la copia original con la modificada), False en caso contrario.
registro_actualizado = actualizar_calificacion(registro_estudiantes, 'Ana', 'Matematicas', 95)
# comparamos 2 listas
print(f"Se actualizó la calificación de Ana en Matematicas?: {registro_estudiantes != registro_actualizado}")
registro_estudiantes = registro_actualizado
mostrar_registro(registro_estudiantes)