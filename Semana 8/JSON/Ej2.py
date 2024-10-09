import json

archivo_original = 'pokemones.json'

def cargar_archivo():
    try:
        with open (archivo_original, 'r') as file:
            pokemones = json.load(file)  #cargar el archivo
    except (FileNotFoundError, json.JSONDecodeError):
        pokemones = []
    return pokemones

def guardar_datos(pokemones):
    with open(archivo_original, 'w') as file:
        json.dump(pokemones, file, indent = 4)   #convertir a JSON

def agregar_datos():
    nombre = input("Ingrese el nombre del pokemon que desea agregar: ")
    tipo = input("Ingrese el tipo del pokemon: ")

    hp = int(input("Ingrese los puntos de salud (HP): "))
    ataque = int(input("Ingrese el ataque: "))
    defensa = int(input("Ingrese la defensa: "))
    sp_attack = int(input("Ingrese el ataque especial: "))
    sp_defense = int(input("Ingrese la defensa especial: "))
    velocidad = int(input("Ingrese la velocidad: "))

    nuevo_pokemon = {
        "name": {"english": nombre},
        "type": tipo,  
        "base": {
            "HP": hp,
            "Attack": ataque,
            "Defense": defensa,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": velocidad
        }
    }

    pokemones = cargar_archivo()

    pokemones.append(nuevo_pokemon)

    guardar_datos(pokemones)

if __name__ == "__main__":
    agregar_datos()