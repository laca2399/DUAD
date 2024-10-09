#2. Experimente con el concepto de scope:
   # 1. Intente accesar a una variable definida dentro de una función desde afuera.
    #2.  Intente accesar a una variable global desde una función y cambiar su valor.

#Ejercicio 2.1: 

#def num_prueba ():
#   num = 55

#print(num)   #Resultado no es posible ya que no existe globalmente

#Ej 2.2

numb = 55

def cambiar_num ():
    global numb   #no me deja cambiar su valor a no ser que use global para hacerle saber al programa que la usare
    numb += 15

cambiar_num()
print(numb)