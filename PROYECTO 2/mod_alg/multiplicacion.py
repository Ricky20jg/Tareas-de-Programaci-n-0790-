#Hacemos una funcion para multiplicar matrices
def mult_matrices(m1,m2):
    
    if len(m1[0]) == len(m2):
        m3 = []
        #Creamos la matriz de acuerdo a las dimensiones de la multiplicaciond de las otras dos
        for i in range(len(m1)):
            m3.append([])
            for _ in range(len(m2[i])):
                m3[i].append(0)
                
    #multiplicamos los elementos de las dos matrices para obtener la matriz resultante \
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                elemento = 0
                #necesitamos otro iterador para multiplicar los elementos alternos de las matrices
                for b in range(len(m2)):
                    elemento = m1[i][b] * m2 [b][j]
                m3[i][j] = elemento
                
        for i in range(len(m3)):
            print(m3[i])
    else:
        raise ValueError ("Las filas de la matriz A deben ser iguales a las columas de la amtriz B")
    
    return m3
