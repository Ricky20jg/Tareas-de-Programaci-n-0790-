def val_lista(ls, length=None, option=None):
    # Comprobamos si el argumento es una lista
    if str(type(ls)) == list:
        # Si no se proporcionan ni longitud ni opción, simplemente devolvemos True
        if length is None and option is None:
            return True
        # Sise proporciona una opción, debemos verificarla
        elif option is not None:
            # Si la opción es "len", comprobamos si la longitud de la lista es igual a la longitud proporcionada
            if option == "len":
                if len(ls) == length:
                    return True
                else:
                    return False
            # Si la opción es "value", comprobamos si la lista es igual a la lista proporcionada
            elif option == "value":
                # Comprobamos si la longitud es una lista
                if str(type(length)) == list:
                    if ls == length:
                        return True
                    else:
                        return False
                else:
                    raise TypeError("El tercer argumento debe ser una lista de valores")
            # Si la opción no es "len" ni "value", lanzamos una excepción
            else:
                raise ValueError("La opción debe ser 'len' o 'value'")
        # Si se proporciona una longitud pero no una opción, simplemente devolvemos True
        elif length is not None:
            return True
    else:
        return False
