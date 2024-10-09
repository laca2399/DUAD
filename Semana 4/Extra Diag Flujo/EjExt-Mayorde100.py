temporal = 0
contador = 1
while(contador<=100):
    num = float(input(f"Ingrese 100 números, 1 a la vez, {contador}: "))
    if(num>temporal):
        temporal = num
    contador = contador + 1
print(f"El mayor es {temporal}")