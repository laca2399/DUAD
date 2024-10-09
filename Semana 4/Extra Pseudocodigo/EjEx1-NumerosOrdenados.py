temporal = 0
primero = float(input("Ingrese un número "))
segundo = float(input("Ingrese otro número "))
if (primero > segundo):
    temporal = primero
    primero = segundo
    segundo = temporal
    print(f"Los números ordenados de menor a mayor se ven así: {primero}, {segundo}")
else:
    print(f"Los números ordenados de menor a mayor se ven así: {primero}, {segundo}")