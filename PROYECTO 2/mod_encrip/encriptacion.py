import random

# Diccionario de sustitución
char_sustitucion = {
    "z": "sT",
    "y": "Wb",
    "x": "Ux",
    "w": "Yk",
    "v": "1p",
    "u": "EA",
    "t": "Hm",
    "s": "2t",
    "r": "Pf",
    "q": "Ce",
    "p": "Fy",
    "o": "M9",
    "ñ": "Bq",
    "n": "5q",
    "m": "Qx",
    "l": "XV",
    "k": "jK",
    "j": "J8",
    "i": "7a",
    "h": "wL",
    "g": "3E",
    "f": "da",
    "e": "Nn",
    "d": "iu",
    "c": "69",
    "b": "hD",
    "a": "-8",
    "9": "5-",
    "8": "/*",
    "7": "+-",
    "6": "h?",
    "5": "/g",
    "4": "#f",
    "3": "*d",
    "2": "we",
    "1": "gh",
    "0": "8J[]"
}

# Función para encriptar
def encriptar(frase):
    cifrado = ""
    for char in frase:
        if char.lower() in char_sustitucion:
            cifrado += char_sustitucion[char.lower()]
        else:
            cifrado += char
    return cifrado

# Función para desencriptar
def desencriptar(frase):
    decifrado = ""
    i = 0
    while i < len(frase):
        char = frase[i:i+2]
        for key, value in char_sustitucion.items():
            if char == value:
                decifrado += key
                i += 2
                break
        else:
            decifrado += frase[i]
            i += 1
    return decifrado

print("Bienvenido al sistema de encriptado\n\n")

opcion = None

while opcion != '1' and opcion != '2':
    opcion = input("Marque 1 si desea encriptar\nMarque 2 si desea desencriptar\n\nIngrese su opción: ")
    if opcion != '1' and opcion != '2':
        print("Ingrese un valor válido.")

if opcion == '1':
    print("Sistema de encriptado\n")
    mensaje = input("Ingrese una frase: ")
    mensaje_encriptado = encriptar(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)

elif opcion == '2':
    print("Sistema de desencriptado\n")
    mensaje_encriptado = input("Ingrese el mensaje encriptado: ")
    mensaje_desencriptado = desencriptar(mensaje_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)