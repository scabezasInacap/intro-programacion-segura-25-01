# descuento de 15% con compras superiores a 50.000

montoDescuento = 15 / 100 # 0.15
montoAplicarDescuento = 50000

montoCompra = int(input("Ingrese el monto de la compra: "))

if (montoCompra > montoAplicarDescuento):
    #se calcula el descuento
    calculoDescuento = montoCompra * montoDescuento
    totalPago = montoCompra - calculoDescuento
    print("El total del pago es $", totalPago, " se hizo un descuento de $", calculoDescuento)
else:
    totalPago = montoCompra
    print("El total del pago es $", totalPago)

# print("El total del pago es $", totalPago)
