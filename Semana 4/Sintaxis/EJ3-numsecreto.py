respuesta = 0
secreto = 7
while (respuesta != secreto):
    num = int(input("Para adivinar el número secreto, ingrese un número entre 1 y 10 "))
    if (num == secreto):
        respuesta = num
        print("Ha acertado")
    else:
        respuesta = num
        print("Vuelva a intentarlo")