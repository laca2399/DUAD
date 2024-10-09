num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese un número "))
num3 = int(input("Ingrese un número "))

if (num1 > num2 and num1 > num3):
    print(f"El mayor es {num1}")
elif(num2 > num1 and num2 > num3):
    print(f"El mayor es {num2}")
elif(num3>num1 and num3>num2):
    print(f"El mayor es {num3}")
else:
    print("Todos son del mismo valor")