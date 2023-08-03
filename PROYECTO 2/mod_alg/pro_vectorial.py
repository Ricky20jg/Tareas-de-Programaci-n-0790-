#creamos la funcion restar
def resta(arg1,arg2):
    arg3 = arg1 - arg2
    return arg3


# vamos a realizar la funcion de producto vectorial
def producto_vectorial(v1, v2):
    
    if (len(v1) == 3) and (len(v2) == 3):
        #establezco un vector donde agrego los resultados 
        v3 = [0,0,0]
        
        #Recordando la forma del producto vectorial y usando la funcion anterior, calculamos los elementos del vector perpendicular
        
        v3[0] = resta((v1[1] * v2[2]),(v1[2]*v2[1]))
        v3[1] = resta((v1[2] * v2[0]),(v1[0]*v2[2]))
        v3[2] = resta((v1[0] * v2[1]),(v1[1]*v2[0]))
        
        print(f""" El vector resutalte del producto vectorial es: 
        [i, j, k]
v3 =    [{v1[0]}, {v2[1]}, {v1[2]}]   =   [{v3[0]}i, {v3[1]}j, {v3[2]}k]
        [{v2[0]}, {v2[1]}, {v2[2]}]""")
        
    else:
        raise TypeError("Los vectores deben ser de dimension = 3")
    
    return v3
