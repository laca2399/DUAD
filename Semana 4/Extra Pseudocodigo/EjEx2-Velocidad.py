metros = 0
segundos = 0
velocidad = float(input("Ingrese la velocidad en km/h: "))
metros = velocidad * 1000
segundos = metros / 3600
print(f"Su velocidad convertida a m/s es de {segundos}")