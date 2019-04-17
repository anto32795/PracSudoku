tablero_input = [
    [5, 3, 0],
    [0, 0, 2],
    [1, 0, 8],
]

soluciones_sudoku = 0

def estaLibre(fila,columna):
    if tablero_input[fila][columna] == 0:
        return True
    else:
        return False
def obten_fila(tablero, indice):
    return tablero[indice]


def obten_columna(tablero, indice):
    rtn = []
    for i in range(0, 3):
        rtn.append(tablero[i][indice])
    return rtn

def obtenCaja(tablero, fila, columna):
    if 0 <= fila <= 2:
        if 0 <= columna <= 2:
            caja_aux = [fil[0:3] for fil in tablero[0:3]]
        elif 3 <= columna <= 5:
            caja_aux = [fil[0:3] for fil in tablero[3:6]]
        elif 6 <= columna <= 8:
            caja_aux = [fil[0:3] for fil in tablero[6:9]]

    elif 3 <= fila <= 5:
        if 0 <= columna <= 2:
            caja_aux = [fil[3:6] for fil in tablero[0:3]]
        elif 3 <= columna <= 5:
            caja_aux = [fil[3:6] for fil in tablero[3:6]]
        elif 6 <= columna <= 8:
            caja_aux = [fil[3:6] for fil in tablero[6:9]]

    elif 6 <= fila <= 8:
        if 0 <= columna <= 2:
            caja_aux = [fil[6:9] for fil in tablero[0:3]]
        elif 3 <= columna <= 5:
            caja_aux = [fil[6:9] for fil in tablero[3:6]]
        elif 6 <= columna <= 8:
            caja_aux = [fil[6:9] for fil in tablero[6:9]]

    return caja_aux

def unicoEnCaja(caja, elem): #falla aqui
    for i in range(0, 3):
        for j in range(0, 3):
            if caja[i][j] == elem:
                return False
    return True

def candidatoEsValido(fila, columna, num_candidato):
    for i in range(0, 3):
        if fila[i] == num_candidato:
            return False
    for i in range(0, 3):
        if columna[i] == num_candidato:
            return False
    return True

'''def is_safe(n, r, c):
    #checking in row
    for i in range(0,3):
        #there is a cell with same value
        if tablero_input[r][i] == n:
            return False
    #checking in column
    for i in range(0,3):
        #there is a cell with same value
        if tablero_input[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
    #checking submatrix
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if tablero_input[i][j]==n:
                return False
    return True'''


def resuelveTablero(celdas,fila,columna):
    if estaLibre(fila,columna):
        for k in range(1,10):
            fila_parametro = obten_fila(celdas, fila)
            columna_parametro = obten_columna(celdas, columna)
            if unicoEnCaja(tablero_aux, k) and candidatoEsValido(fila_parametro,columna_parametro,k):
                #if is_safe(k,fila,columna)
                celdas[fila][columna] = k
                if fila == 2 and columna == 2:
                    global soluciones_sudoku
                    soluciones_sudoku = soluciones_sudoku +1
                elif fila<2 and columna==2:
                    resuelveTablero(celdas,fila+1,0) #poner columna a columna
                else:
                    resuelveTablero(celdas,fila,columna+1)
                celdas[fila][columna] = 0

    else:
        if fila == 2 and columna == 2:
            soluciones_sudoku = soluciones_sudoku +1
        elif fila < 2 and columna == 2:
            resuelveTablero(celdas, fila+1,0)
        else:
            resuelveTablero(celdas,fila,columna+1)


tablero_aux = tablero_input.copy()
resuelveTablero(tablero_aux,0,0)

print(soluciones_sudoku)

