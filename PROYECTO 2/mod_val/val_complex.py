# Primera función: Validar un número complejo
def val_complex(num, interval=None):
    # Comprobamos si el número es un complejo
    if str(type(num)) == complex:
        # Si no se proporciona un intervalo, simplemente devolvemos True
        if interval is None:
            return True
        # Si se proporciona un intervalo, comprobamos si el módulo del número está en el intervalo
        else:
            # Comprobamos si el intervalo es una lista o una tupla de dos elementos
            if (str(type(interval)) == list or str(type(interval)) == tuple) and len(interval) == 2:
                # Comprobamos si el intervalo está ordenado de manera creciente
                if interval[0] < interval[1]:
                    # Calculamos el módulo del número
                    mod = (num.real * num.real + num.imag * num.imag) ** 0.5
                    # Comprobamos si el módulo está dentro del intervalo
                    if interval[0] < mod and mod < interval[1]:
                        return True
                    else:
                        return False
                else:
                    raise ValueError("El intervalo debe estar ordenado de manera creciente")
            else:
                raise TypeError("El segundo argumento debe ser una lista o tupla de dos números")
    else:
        return False

