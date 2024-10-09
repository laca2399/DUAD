contador = 1
cant_homb = 0
cant_muj = 0
porc_homb = 0
porc_muj = 0
while(contador <= 6):
    sexo = int(input(f"Ingrese el sexo de 6 personas, digite 1 si es mujer o 2 si es hombre, persona #{contador}: "))
    if (sexo == 1):
        cant_muj = cant_muj + 1
    else:
        cant_homb = cant_homb + 1
    contador = contador + 1
porc_muj = (cant_muj / 6) * 100
porc_homb = (cant_homb / 6) * 100
print(f"El porcentaje de mujeres es de {porc_muj}%")
print(f"El porcentaje de hombres es de {porc_homb}%")