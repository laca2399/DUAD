#Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


def open_and_print_file_per_line(path):
    with open(path, encoding="utf-8") as file:
        return file.readlines()  

def ordenar_canciones(original_path, new_path):
    canciones = open_and_print_file_per_line(original_path)
    canciones.sort()

    with open(new_path, "w", encoding="utf-8") as new_file:
        for cancion in canciones:
            new_file.write(cancion)  

    return canciones  

def imprimir (path):
    print(f'Contenido de {path}:')
    with open(path, encoding="utf-8") as file:
        for line in file:
            print(line, end='')

input_file = 'canciones.txt'  
output_file = 'nuevo.txt' 

#input_file = 'D:/Users/ANDRES LACAYO/Documents/Progra/canciones.txt'  
#output_file = 'D:/Users/ANDRES LACAYO/Documents/Progra/nuevo.txt'  

ordenar_canciones(input_file, output_file)
imprimir(input_file)
imprimir(output_file)