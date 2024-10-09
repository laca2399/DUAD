nombre = input("Ingrese su nombre ")
apellido = input ("Ingrese su apellido ")
edad = int(input("Ingrese cuantos años tiene "))

if (edad <= 5):
    print("Es un bebé")
elif(edad <=11):
    print("Es un niño")
elif(edad<=15):
    print("Es un preadolescente")
elif(edad<=18):
    print("Es un adolescente")
elif(edad<=30):
    print("Es un adulto joven")
elif(edad<=60):
    print("Es un adulto")
else:
    print("Es un adulto mayor")