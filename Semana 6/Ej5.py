#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string

def conteo_mayus_minus(string):
    mayus = sum(1 for letra in string if letra.isupper())
    minus = sum(1 for letra in string if letra.islower())

    print(f"El número de mayúsculas es: {mayus}")
    print(f"El número de minúsculas es: {minus}")

conteo_mayus_minus("I Love Nación Sushi")