import random

def matriz_propia():
    
    n = int(input("Diga el número de filas: "))
    m = int(input("Diga el número de columnas: "))
    
    matriz = []
    
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = int(input(f"Ingrese el elemento en la posición [{i+int(1)}][{j+int(1)}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    for fila in matriz:
        print(fila)
        
    return matriz
        
def matriz_random():
    
    n = int(input("Ingresa el número de filas: "))
    m = int(input("Ingresa el número de columnas: "))

    if (type(m) == str or type(n) == str):
        print("Ingrese datos numéricos.")
    else:
        # Establecer la matriz
        matriz = []

        for _ in range(n):
            fila= []
            for _ in range(m):
                fila.append(random.randint(1, 100))
            matriz.append(fila)

        # Imprimir la matriz
        for i in range(n):
            print(matriz[i])
            
    return matriz
    
def matriz_secuencia():
    n = int(input("Diga el número de filas: "))
    m = int(input("Diga el número de columnas: "))

    if (type(m) == str or type(n) == str):
        print("Ingrese datos numéricos.")
        return None

    else:
        # Establecer la matriz
        matriz = []

        for _ in range(n):
            fila = []
            for _ in range(m):
                fila.append(0)
            matriz.append(fila)

        # Agregar valores secuenciales a la matriz
        a = 1
        for i in range(n):
            for j in range(m):
                matriz[i][j] = a
                a += 1

        # Imprimir la matriz generada
        for i in range(n):
            print(matriz[i])
            
    return matriz