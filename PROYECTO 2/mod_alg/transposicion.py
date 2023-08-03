def matriz_transpuesta(m1):
    #Aplicamos el caso para matrices cuadradas
    if len(m1) == len(m1[0]):
        
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m1[i][j] = m1 [j][i]
                
        for i in range(len(m1)):
            print(m1[i])
        return m1
            
    elif len(m1) != len(m1[0]):
        transpuesta = []
        
        for i in range(len(m1[0])):
            transpuesta.append([])
            for j in range(len(m1)):
                transpuesta[i].append(0)
                
                transpuesta[i][j] = m1[j][i]
        
                
        for i in range(len(transpuesta)):
            print(transpuesta[i])
        return transpuesta