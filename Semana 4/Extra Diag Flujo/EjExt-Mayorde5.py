temporal = 0
contador = 1
while(contador<=5):
    num = float(input(f"Ingrese 5 números, 1 a la vez, {contador}: "))
    if(num>temporal):
        temporal = num
    contador = contador + 1
print(f"El mayor es {temporal}")