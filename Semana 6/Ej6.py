#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
 #   1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
  #  2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def ordenar_palabras(string):
    palabras = string.split("-")
    palabras.sort()
    resultado = "-".join(palabras)
    return resultado



resultado = ordenar_palabras("python-variable-funcion-computadora-monitor")
print(resultado)

