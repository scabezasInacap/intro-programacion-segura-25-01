#agragar el bucle para continuar ingresando datos
opt=1
while (opt==1):
    #ingresar cantidad de amigos
    cantidadAmigos = int(input("Ingrese cantidad de Amigos: "))
    if cantidadAmigos > 0:
        #definir los precios
        precioPitcher = 7000
        precioChorrillana = 8000
        precioPapasFritas = 4000
        porcentajePropina = 0.1
        #solicitar al usuario la cantidad consumida
        cantidadPitcher = -1
        while cantidadPitcher < 0:
            cantidadPitcher = int(input("Ingrese Cantidad Consumida de Pitcher: "))
            if cantidadPitcher < 0:
                print("Error: Debe ingresar un numero mayor que 0")
        cantidadChorrillana = int(input("Ingrese Cantidad Consumida de Chorrillanas: "))
        cantidadPapasFritas = int(input("Ingrese Cantidad Consumida de Papas Fritas: "))
        #calcular el subtotal
        subTotal = cantidadPitcher*precioPitcher + cantidadChorrillana*precioChorrillana + cantidadPapasFritas * precioPapasFritas
        #calcular el monto de la propina
        montoPropina = subTotal * porcentajePropina
        #calcular cuanto debe pagar cada uno
        montoPagarCadaUno = (subTotal + montoPropina) / cantidadAmigos
        #mostramos cuanto debe pagar cada uno
        print("El total de la cuenta es $" , subTotal, ", la propina es $", montoPropina, ", cada uno deberá pagar $", montoPagarCadaUno)
    else:
        print("No hay nada que hacer, si no hay personas en el bar")
    opt = int(input("Si desea continuar, ingrese 1, en caso de salir, presione otro numero: "))
print("Fin del Programa")
