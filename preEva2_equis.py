# Para _n = 7, _cx = 1, _co = 0
# 10000001
# 01000010
# 00100100
# 00011000
# 00100100
# 01000010
# 10000001

# Para _n = 6, _cx = 'x', _co = ' '
# 1    1
#  1  1 
#   11  
#  1  1 
# 1    1

# Para _n = 7, _cx = 1, _co = 0
# 10000001
# 01000010
# 00100100
# 00011000
# 00100100
# 01000010
# 10000001

# Para _n = 6, _cx = 'x', _co = ' '
# 1    1
#  1  1 
#   11  
#  1  1 
# 1    1


def imprimeX(_n, _cx, _co):
    # print(f"{_n}{_cx}{_co}")
    fila = 0
    while (fila < _n):
        columna = 0
        while (columna < _n):
            if (fila == columna or (fila + columna == _n-1)):
                print(f"{_cx}", end="")
            else:
                print(f"{_co}", end="")
            columna += 1
            if (columna == _n):
                print()
        fila += 1
#APP
imprimeX(7, 1,0)
print()
imprimeX(7, 'X', ' ')
imprimeX(8, 'X', ' ')
imprimeX(50, 'X', ' ')
