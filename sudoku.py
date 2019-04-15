soluciones_sudoku = 0

tablero_input = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 0, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 4, 0, 0, 6],
    [0, 6, 1, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


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
    for i in range(0, 9):
        if fila[i] == num_candidato:
            return False
    for i in range(0, 9):
        if columna[i] == num_candidato:
            return False
    return True


def quedanHuecosLibres(tablero):
    for i in range(0, 9):
        for j in range(0, 9):
            if tablero[i][j] == 0:
                return True
    return False


def obten_fila(tablero, indice):
    return tablero[indice]


def obten_columna(tablero, indice):
    rtn = []
    for i in range(0, 9):
        rtn.append(tablero[i][indice])
    return rtn


def resuelveTablero(tablero, soluc_parcial, lista_candidatos):
    if (not quedanHuecosLibres(soluc_parcial)):  # encontrada una solucion
        global soluciones_sudoku
        soluciones_sudoku = soluciones_sudoku + 1
    else:
        for i in range(0, 9):
            for j in range(0, 9):
                if tablero[i][j] == 0:
                    for k in range(0, len(lista_candidatos)):
                        candidato = lista_candidatos[k]  # generar candidato k-esimo
                        fila_parametro = obten_fila(tablero, i)
                        columna_parametro = obten_columna(tablero, j)
                        if unicoEnCaja(obtenCaja(tablero, i, j), candidato) and candidatoEsValido(fila_parametro,
                                                                                                  columna_parametro,
                                                                                                  candidato):
                            soluc_parcial[i][j] = candidato
                            resuelveTablero(tablero, soluc_parcial, lista_candidatos)

                            soluc_parcial[i][j] = 0


sol_p = tablero_input.copy()
resuelveTablero(tablero_input,sol_p,[1,2,3,4,5,6,7,8,9])
print(soluciones_sudoku)
