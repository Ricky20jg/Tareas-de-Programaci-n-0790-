def determinante(m1):
    filas = len(m1)
    columnas = len(m1[0])
    #debemos asegurarnos de que la matriz sea una matriz cuadrada.
    
    if filas != columnas:
        raise ValueError("El número de filas debe ser igual al número de columnas.")

    # Para el caso de matrices 2x2
    elif filas == 2 and columnas == 2:
        return m1[0][0] * m1[1][1] - m1[0][1] * m1[1][0]

    det = 0
    if (filas > 2) and (columnas > 2) and (filas==columnas):
    #Utilizando el metodo de cofactores haciendo una submatriz   
        for j in range(columnas):
            submatriz = []
            
            #partiendo desde 1 hasta filas, eliminamos una columna para añadir los elementos
            
            for i in range(1, filas):
                fila_actualizada = []

                for k in range(columnas):
                    if k != j:
                        fila_actualizada.append(m1[i][k])
                
                submatriz.append(fila_actualizada)
            #los elementos de la matriz deben ser multiplicadas por un cofactor que se alterna para 
            cofactor = (-1) ** (j % 2) * determinante(submatriz)
            det += m1[j][0] * cofactor

        return det