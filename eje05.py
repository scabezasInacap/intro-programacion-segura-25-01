import copy
#Ejercicio 5: Recetas de Cocina
#Descripción: Crea un recetario simple donde cada receta es un diccionario con
#  ingredientes (lista) e instrucciones.

#Instrucciones:
#[OK] Crea una lista vacía llamada recetario.
#[OK] Define una función mostrar_recetario(recetario_actual) que imprima el nombre de la receta,
#  sus ingredientes y sus instrucciones.
#Añade las siguientes recetas (diccionarios) a la lista:
#[] {"nombre": "Pasta Carbonara", "ingredientes": ["Pasta", "Huevo", "Panceta", "Parmesano"], "instrucciones": "Mezclar todo..."}
#{"nombre": "Sopa de Lentejas", "ingredientes": ["Lentejas", "Zanahoria", "Cebolla"], "instrucciones": "Cocer lentamente..."}
#Imprime el recetario después de cada adición.
#Crea una función añadir_ingrediente(recetario, nombre_receta, nuevo_ingrediente) que 
# añada un ingrediente a una receta existente. 
# Utiliza deepcopy() para copiar el recetario antes de la modificación y retorna True
#  si el ingrediente fue añadido exitosamente.
#Añade "Ajo" a la receta "Sopa de Lentejas". Muestra si se añadió el ingrediente.
#Imprime el recetario final.
#Salida Esperada:
#[OK]
#--- Recetario de Cocina ---
#El recetario está vacío.

#--- Recetario de Cocina ---
#Receta: Pasta Carbonara
#  Ingredientes: ['Pasta', 'Huevo', 'Panceta', 'Parmesano']
#  Instrucciones: Mezclar todo...
#--- Recetario de Cocina ---
#Receta: Pasta Carbonara
#  Ingredientes: ['Pasta', 'Huevo', 'Panceta', 'Parmesano']
#  Instrucciones: Mezclar todo...
#Receta: Sopa de Lentejas
#  Ingredientes: ['Lentejas', 'Zanahoria', 'Cebolla']
#  Instrucciones: Cocer lentamente...
#Se añadió "Ajo" a la receta "Sopa de Lentejas": True
#--- Recetario de Cocina ---
#Receta: Pasta Carbonara
#  Ingredientes: ['Pasta', 'Huevo', 'Panceta', 'Parmesano']
#  Instrucciones: Mezclar todo...
#Receta: Sopa de Lentejas
#  Ingredientes: ['Lentejas', 'Zanahoria', 'Cebolla', 'Ajo']
#  Instrucciones: Cocer lentamente...

#PASO 2: Define una función mostrar_recetario(recetario_actual) que imprima el nombre de
#  la receta, sus ingredientes y sus instrucciones.
def mostrar_recetario(recetario_actual):
    print("--- Recetario de Cocina ---")
    if (len(recetario_actual) == 0):
        print("El recetario está vacío.")
    else:
        for receta in recetario_actual:
            #print(receta)
            print(f"Receta: {receta['nombre']}\n - Ingredientes: {receta['ingredientes']}")
            print(f" - Instrucciones: {receta['instrucciones']}")
    print("")

def añadir_ingrediente(recetario, nombre_receta, nuevo_ingrediente):
    nuevaLista = copy.deepcopy(recetario)
    for receta in nuevaLista:
        if (receta['nombre'] == nombre_receta):
            receta['ingredientes'].append(nuevo_ingrediente)
            #print(receta['ingredientes'])
            break
    return nuevaLista


#PASO 1: Crea una lista vacía llamada recetario.
recetario = []
mostrar_recetario(recetario)
dic = {"nombre": "Pasta Carbonara", "ingredientes": ["Pasta", "Huevo", "Panceta", "Parmesano"], "instrucciones": "Mezclar todo..."}
recetario.append(dic)
mostrar_recetario(recetario)
dic = {"nombre": "Sopa de Lentejas", "ingredientes": ["Lentejas", "Zanahoria", "Cebolla"], "instrucciones": "Cocer lentamente..."}
recetario.append(dic)
mostrar_recetario(recetario)

#Crea una función añadir_ingrediente(recetario, nombre_receta, nuevo_ingrediente) que 
# añada un ingrediente a una receta existente
recetarioActualizado = añadir_ingrediente(recetario, 'Sopa de Lentejas', 'Ajo')
print(f"Se hicieron cambios? {recetario != recetarioActualizado}")
recetario = recetarioActualizado
mostrar_recetario(recetario)