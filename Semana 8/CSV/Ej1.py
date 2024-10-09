import csv
#Función para ingresar los datos
def ingresar_datos ():
    nombre = input("Ingrese el nombre del videojuego: ")
    genero = input("Ingrese el genero del videouego: ")
    desarrollador = input("Ingrese el desarrollador del videojuego: ")
    clasificacion = input("Ingrese la clasificación ESRB del videojuego: ")

    return {
        "Nombre": nombre,
        "Genero": genero,
        "Desarrollador": desarrollador,
        "Clasificacion": clasificacion
    }
#Función para guardar datos en un archivo con el uso de Escritura
def guardar_datos(archivo, videojuegos):

    nombres_columnas = ["Nombre", "Genero", "Desarrollador", "Clasificacion"]

    with open(archivo, 'w', newline='', encoding='utf-8' ) as file:
        writer=csv.DictWriter(file, fieldnames=nombres_columnas)
        writer.writeheader()
        writer.writerows(videojuegos)

    print(f"Los datos se han guardado en {archivo} de manera exitosa")


def main ():
    cantidad_videojuegos = int(input("Ingrese la cantidad de videojuegos que desea guardar: "))
    videojuegos = []

    for i in range (cantidad_videojuegos):
        print(f"Videojuego #{i+1}: ")
        videojuego = ingresar_datos()
        videojuegos.append(videojuego)
        i +=1

    archivo_csv = "videojuegos.csv"
    guardar_datos(archivo_csv, videojuegos)

if __name__ == "__main__":
    main()



