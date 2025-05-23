# $ $ $ $ $ $ $
# $ $ $ * $ $ $ 
# $ $ * * * $ $
# $ * * * * * $
# $ $ * * * $ $
# $ $ $ * $ $ $
# $ $ $ $ $ $ $


# Considera la condición de borde para ingresar un numero y representar la figura
# La función debe recibir 3 valores como parámetros: _caracterInterior, _caracterExterior, _numero
# Debe validar que el numero ingresado sea solo un numero impar.
# Debe validar que caracter interior y caracter exterior solo tenga un caracter.

# Evaluacion 2:
# Sentencias de control: If, Else, Elif
# Control de ciclos: While, For
# Funciones

def imprimeFigura(_ci, _ce, _n):
    #print(f"ci: {_ci} ce: {_ce} n: {_n}")
    iterador = 0
    while iterador < _n:
        mitad = int(_n/2)
        if (iterador == 0 or iterador == (_n -1)):
            print(f"{_ce * _n}")
        else:
            if (iterador <= mitad):
                cantidadInterior = (iterador + (1 * iterador) - 1)
            else:
                cantidadInterior = cantidadInterior - 2
            cantidadMitadExterior = int((_n - cantidadInterior)/2)
            print(f"{_ce * cantidadMitadExterior}{_ci * cantidadInterior}{_ce * cantidadMitadExterior}")
        iterador += 1

#APP
imprimeFigura(' ','#',21)
