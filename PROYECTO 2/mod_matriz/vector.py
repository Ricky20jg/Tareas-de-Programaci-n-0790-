#funcion par hacer vectores
import random

def vector_random():
    vector=[]
    n = int(input("De cuantas dimensiones será el vector:  "))
    
    for _ in range(n):
        vector.append(random.randint(0,100))
        
    return vector

def vector_propio():
    vector = []
    n = int(input("De Cuantas dimensiones será el vector:  "))
    
    for i in range (n):
        elemento = int(input(f"indique el elemento [{i+int(1)}]:  "))
        vector.append(elemento)
        
    print(vector)
    
    return vector

def vector_secuencia():
    vector = []
    n = int(input("De Cuantas dimensiones será el vector:  "))
    
    a = 1
    for _ in range(n):
        vector.append(a)
        a += 1
        
    print(vector)
    
    return vector