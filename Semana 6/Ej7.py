def es_primo(num):
    for n in range (2,num):
        if num % n == 0:
            return False
        return True


def filtrar_pri(numeros):
    return [num for num in numeros if es_primo(num)]

lista=[1, 4, 6, 7, 13, 67] 
primos = filtrar_pri(lista)
print(primos)

