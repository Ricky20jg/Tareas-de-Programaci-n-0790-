#Suma de vectores

def suma_vectores(v1,v2):
    #Debemos verificar que ambos vectores tengan las mismas dimensiones
    if len(v1) == len(v2):
        #se crea un tercer vector que albergará las sumas de los elementos en la posicion i
        v3 = []
        for i in range (len(v1)):
            v3.append(v1[i]+v2[i])
        print (v3)
        
    #Si no son iguales levantamos un error 
    else:
        raise TypeError("No se pueden sumar vectores de diferentes dimensiones")
    
    return v3
    
#Ahora desarrollamos la suma de matrices

def suma_matriz(m1, m2):
    #Se verifica que tengan igual numero de filas y columnas
    if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
        #creamos una matriz que le albergamos ceros
        m3 = []
        
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[i])):
                m3[i].append(0)
        
        #ahora en cada elemento [i][j] de m3 se realizará la suma de los elementos [i][j] de m1 y m2         
        for i in range(len(m3)):
            for j in range(len(m3[i])):
                m3[i][j] = m1[i][j] + m2 [i][j]
        
        #imprimimos la matriz para formalizar la suma
        for i in range(len(m3)):
            print(f"{m1[i]}  +   {m2[i]}  =  {m3[i]}")
        
    else:
        raise ValueError("Las matrices no son de iguales dimensiones")
    
    return m3