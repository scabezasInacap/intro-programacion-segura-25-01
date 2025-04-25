# tenemos 3 notas, calcular el promedio, indicar si esta aprobado, reprobado, o buen trabajo y mostrar la nota mas alta
n1 = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 3: "))
x = (n1 + n2 + n3)/3
if (x < 4):
    print("Reprobado con nota: ", x)
elif (x >=4 and x <=7):
    # aprobado
    if (x >= 6 and x <=7):
        print("Aprobado, buen trabajo, con nota: " , x)
    else:
        print("Aprobado con promedio: ", x)
# calcular la nota mas alta
if (n1 >= n2 and n1 >= n3):
    print("Nota mas alta: ", n1)
elif (n2 >= n1 and n2 >= n3):
    print("Nota mas alta: ", n2)
elif (n3 >= n1 and n3 >= n2):
    print("Nota mas alta: ", n3)
