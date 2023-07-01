#La practica no me salio, hice mi intento :(

while True:

    vector_1 = [0]*10
    vector_2 = [0]*10

    binario_1= input("ingres el primer numero binario: ")
    binario_2 = input("Ingrese el segundo numero binario: ")

    while len(binario_1) < 10 and len(binario_2):
        binario_1 = "0" + binario_1
        binario_2 = "0" + binario_2

    print(f"los numeros ingresados son {binario_1} y {binario_2}")

    if binario_1.isnumeric() and binario_2.isnumeric():

        if len(binario_1) > 10 or len(binario_2) > 10:
            raise ValueError("Los numeros requeridos no pueden ser mayores a 10 digitos.")

        else:
        #coloco los digitos del numero binario en el vector, pero antes convierto los numeros en "int"
            binario1_int = int(binario_1)
            binario2_int = int(binario_2)

            for i in range(len(binario_1)):
                vector_1[i]=binario_1[i]
            print(vector_1)

            for i in range(len(binario_2)):
                vector_2[i]=binario_2[i]
            print(vector_2)

            #Establezco un vector 3 que será la suma de ambos:

            vector_3 =[0]*10
            a = 0
            #establezcon un contador que me permitirá ir de derecha a izquierda
            c = 1
            
           
        #Ahora procedemos a sumarlos de acuerdo a los escenarios que den 0 o 1 
        while len(vector_3) == 10 :

            for j in range (len(binario_1)):

                longitud = len(vector_1) - c
                vector_3[longitud] = int(vector_1[longitud]) + int(vector_2[longitud]) + a

                if vector_3[longitud] > 1:

                    vector_1[longitud] = vector_2[longitud] == 0
                    a = 1

                    vector_3[longitud] = int(vector_1[longitud]) + int(vector_2[longitud]) + a

                elif vector_3[longitud] == 1 or vector_3[longitud] == 0:

                    a = 0
                    vector_3[longitud] = int(vector_1[longitud]) + int(vector_2[longitud])
                    c += 1
                    
                    vector_3.append(vector_3[longitud] % 2)
                    
                elif len(vector_3) >= 11:
                    raise ValueError ("No es posible dar un resultado, el vector pasa de 10 digitos")

                else:
                    raise ValueError("No puede dar numerosm negativos")
                    
        print(vector_3)
    
    else:
        raise ValueError("No ingresó numeros binarios.")