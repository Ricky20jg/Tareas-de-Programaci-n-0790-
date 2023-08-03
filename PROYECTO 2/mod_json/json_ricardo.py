import json

#FUNCION PARA SALVAR LO ESCRITO EN UN ARCHIVO JSON

def save_from_json(data,file_path):
    #la w hace que se sobreescriba el archivo .json
    with open(file_path,  "w") as file:
        json.dump(data, file, indent=2)
        
#Dump

##FUNCION PARA LEER UN JSON EN PYTHON

def read_from_json(file_path):
    data = {}
    with open(file_path) as file:
        data = json.load(data)

def create_json(file_path):
    data = {
    }

    with open(file_path, 'w') as file:
        json.dump(data, file)

