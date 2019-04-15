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


def resuelveTablero(i,j,sol, inicial):
	if inicial[i][j] == False:
		for k in range(0,9):
			sol[i][j] = k
			fila_parametro = obten_fila(sol,i)
			columna_parametro = obten_columna(sol,j)
			if candidatoEsValido(fila_parametro,columna_parametro,k) and unicoEnCaja(obtenCaja(sol,i,j),k):#candidato viable
				if i == 8 and j == 8:
					global soluciones_sudoku
					soluciones_sudoku = soluciones_sudoku + 1
				elif i < 8 and j == 8:
					resuelveTablero(i+1,1,sol,inicial)
				elif i<=8 and j < 8:
					resuelveTablero(i,j+1,sol,inicial)
			sol[i][j] = 0
	else:
		if i == 8 and j == 8:
			global soluciones_sudoku
			soluciones_sudoku = soluciones_sudoku + 1
		elif i < 8 and j == 8:
			resuelveTablero(i+1,1,sol,inicial)
		elif i<=8 and j < 8:
			resuelveTablero(i,j+1,sol,inicial)


sol_p = tablero_input.copy()
resuelveTablero(tablero_input,sol_p,[1,2,3,4,5,6,7,8,9])
print(soluciones_sudoku)