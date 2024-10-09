contador_nota = 1
cant_notas_aprobadas = 0
cant_notas_desaprobadas = 0
prom_notas_aprobadas = 0
prom_notas_desaprobadas = 0
prom_notas_total = 0

total_notas = int(input("Ingrese la cantidad de notas "))
while (contador_nota <= total_notas):
    nota_actual = float(input(f"Ingrese la nota número {contador_nota}: "))
    if (nota_actual < 70):
        cant_notas_desaprobadas = cant_notas_desaprobadas + 1
        prom_notas_desaprobadas = prom_notas_desaprobadas + nota_actual
    else:
        cant_notas_aprobadas = cant_notas_aprobadas + 1
        prom_notas_aprobadas = prom_notas_aprobadas + nota_actual
    prom_notas_total = (prom_notas_desaprobadas + prom_notas_aprobadas) / total_notas
    contador_nota = contador_nota + 1
prom_notas_desaprobadas = prom_notas_desaprobadas / cant_notas_desaprobadas
prom_notas_aprobadas = prom_notas_aprobadas / cant_notas_aprobadas
print(f"El estudiante tiene esta cantidad de notas aprobadas {cant_notas_aprobadas}")
print(f"Este es el promedio de notas aprobadas {prom_notas_aprobadas}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas {cant_notas_desaprobadas}")
print(f"Este es el promedio de notas desaprobadas {prom_notas_desaprobadas}")
print(f"Este es el promedio total de notas {prom_notas_total}")
