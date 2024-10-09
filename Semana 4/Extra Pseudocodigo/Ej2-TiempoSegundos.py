tiempo_segundos = float(input("Ingrese el tiempo en segundos "))
if (tiempo_segundos <600):
    segundos_falt = 600 - tiempo_segundos
    print(f"Faltan esta cantidad de segundos para llegar a 10 minutos: {segundos_falt}")
else:
    print("Mayor")