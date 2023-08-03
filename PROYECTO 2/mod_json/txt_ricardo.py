
def create_txt(file_path):
    with open (file_path,"x") as file:
        file.readline

#Funcion para leer un Txt

def read_from_txt(file_path):
    if not (file_path):
        raise ValueError("No existe el archivo")
    else: 
        with open(file_path,'r') as file:
            data = file.readlines
            print(data)
    return data

#Funcion para modificar un Txt

def append_to_txt(data,file_path):
    with open (file_path,"a") as file:
        file.write(data)

#Funcion para sobreescribir sobre el  Txt
        
def write_to_txt(data,file_path):
    with open (file_path,"w") as file:
        data = file.writelines(data)
        