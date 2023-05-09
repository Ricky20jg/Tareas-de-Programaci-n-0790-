while True:
    n_1 = input("ingrese un número:")
    n_2 = input("ingrese otro número:")
    if n_1.isnumeric() and n_2.isnumeric():
        print ("la suma de los números es:", float(n_1) + float(n_2))
        break
    else:
        print("no ingresó números, vuelva al inicio.")