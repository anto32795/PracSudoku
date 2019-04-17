'''tablero_input = [
    [0, 3, 0],
    [6, 0, 0],
    [0, 0, 8],
]

tablero_input = [
    [5, 0, 4, 6, 7, 8, 9, 0, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 0, 4, 2, 5, 6, 7],
    [8, 2, 6, 7, 5, 1, 4, 9, 3],
    [4, 5, 9, 8, 6, 3, 7, 2, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 0, 5, 3, 7, 2, 0, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 5, 2, 8, 6, 1, 7, 9]
]
tablero_input = [
    [5, 3, 0, 0, 7, 0],
    [6, 0, 0, 1, 0, 5],
    [0, 9, 8, 0, 0, 0],
    [8, 0, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 3],
    [7, 0, 0, 0, 2, 0]

]'''
tablero_input = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 0, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

soluciones_sudoku = 0

def estaLibre(fila,columna,ma):
    if ma[fila][columna] == 0:
        return True
    else:
        return False



def is_safe(n, r, c,tablero_input):
    #checking in row
    for i in range(0,9):
        #there is a cell with same value
        if tablero_input[r][i] == n:
            return False
    #checking in column
    for i in range(0,9):
        #there is a cell with same value
        if tablero_input[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3
    #checking submatrix
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
                if fila == 8 and columna == 8:
                    global soluciones_sudoku
                    soluciones_sudoku = soluciones_sudoku +1
                elif fila<8 and columna==8:
                    resuelveTablero(celdas,fila+1,0) #poner columna a columna
                else:
                    resuelveTablero(celdas,fila,columna+1)
            celdas[fila][columna] = 0

    else:
        if fila == 8 and columna == 8:
            soluciones_sudoku = soluciones_sudoku + 1
        elif fila < 8 and columna == 8:
            resuelveTablero(celdas, fila+1,0)
        else:
            resuelveTablero(celdas,fila,columna+1)


tablero_aux = tablero_input.copy()
resuelveTablero(tablero_aux,0,0)

print(soluciones_sudoku)

