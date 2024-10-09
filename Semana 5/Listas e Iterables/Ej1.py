#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index, valor in enumerate(first_list):
    print(valor, second_list[index])