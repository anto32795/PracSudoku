def resuelveCaja(caja,lista_candidatos):
	for i in range(0,3):
		for j in range(0,3):
			if caja[i][j] == 0:
				for k in range(0,len(lista_candidatos)):
					caja[i][j] = lista_candidatos[k]
					if cajaValido() and filaColumnaValido(fila=caja[i],columna=?):
						lista_candidatos[k].remove
						resuelveCaja(caja,lista_candidatos)