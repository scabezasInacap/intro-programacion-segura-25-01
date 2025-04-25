# Sala de servidores entre 18°C y 22° C

tempMinima = 18
tempMaxima = 22

temperaturaActual = int(input("Ingrese la temperatura actual de la sala de servidores: "))

if (temperaturaActual < tempMinima):
    print("Encender Calefacción")
elif (temperaturaActual > tempMaxima):
    print("Encender Aire Acondicionado")
else:
    print("No hace nada... la temperatura esta correcta entre ",tempMinima," y ",tempMaxima," °C")
