soluciones_sudoku = 0

def estaLibre(fila,columna,ma):
    if ma[fila][columna] == 0:
        return True
    else:
        return False



def is_safe(n, r, c,tablero_input):
    #comprobando en fila
    for i in range(0,9):
        if tablero_input[r][i] == n:
            return False
    #comprobando columna
    for i in range(0,9):
        if tablero_input[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3
    #comprobar cajas
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if tablero_input[i][j]==n:
                return False
    return True


def resuelveTablero(celdas,fila,columna):
    if estaLibre(fila,columna,celdas):
        for k in range(1,10):
            if is_safe(k,fila,columna,celdas):

                celdas[fila][columna] = k
                if fila == 8 and columna == 8:                  #si tablero completo -> encontrada una solucion
                    global soluciones_sudoku
                    soluciones_sudoku = soluciones_sudoku +1
                elif fila<8 and columna==8:                     #faltan filas por rellenar
                    resuelveTablero(celdas,fila+1,0)
                else:
                    resuelveTablero(celdas,fila,columna+1)
            celdas[fila][columna] = 0

    else:
        if fila == 8 and columna == 8:                          #si tablero completo -> encontrada una solucion
            soluciones_sudoku = soluciones_sudoku + 1
        elif fila < 8 and columna == 8:
            resuelveTablero(celdas, fila+1,0)
        else:
            resuelveTablero(celdas,fila,columna+1)


tablero_input = []
#entrada del algoritmo

for i in range(0,9):
    palabra = input()
    vector = palabra.split()
    vector = [int(i) for i in vector]
    tablero_input.append(vector)

tablero_aux = tablero_input.copy()
resuelveTablero(tablero_aux,0,0)

print(soluciones_sudoku)