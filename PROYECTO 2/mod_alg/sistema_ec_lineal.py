#Dado un sistema de ecuaciones de la siguiente forma:

# ax + by = c
# dx + ey = f

def sistema_ecuaciones(a,b,c,d,e,f):
    a = float(input("Inidique el valor de a: "))
    b = float(input("Inidique el valor de b: "))
    c = float(input("Inidique el valor de la constante c: "))
    d = float(input("Inidique el valor de d: "))
    e = float(input("Inidique el valor de e: "))
    f = float(input("Inidique el valor de la constante f: "))
    
    print(f"""el sitema de ecuaciones estado por:

{a}x + {b}y = {c}
{d}x + {d}y = {f}
""")
    #calculamos el determinante para verificar si hay solucion
    det = a*e - b*d
    
    if det != 0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        return x, y
    else:
        print("El sistema de ecuaciones no tiene solucion")