contador = 1
suma = 0
while(contador<=100):
    num = float(input(f"Ingrese 100 número, 1 a la vez,  #{contador}: "))
    suma = suma+num
    contador = contador + 1
print(f"La suma total de los 100 números ingresados es {suma}")