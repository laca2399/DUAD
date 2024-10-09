#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación

#Primero defini 5 funciones que hacen referencia a 5 de las operaciones del menu

def sumar (x, y):
    return x + y

def restar (x, y):
    return x - y

def multiplicar (x, y):
    return x * y

def dividir (x,y):
    if y !=0:
        return x / y
    else:
        raise ZeroDivisionError ("No se puede dividir un número por cero")
    
def borrar ():
    return 0
    
def menu ():  #Función para mostrar el menú
    print("Seleccione la operación que desea realizar: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Borrar resultado")
    print("6. Salir")

def main():   #la función main es el núcleo de la computadora y a partir de ella se da el funcionamiento
    numero_actual = 0      #definimos el número actual como lo pide el ejercicio
    while True:    #Este while true esta relacionado con el continuar de más abajo...
        menu()
        
        
        operacion = input("Ingrese el número de la operación que desea realizar (1/2/3/4/5/6): ")
        #Este try que es como el general, no lo entiendo muy bien, pero si no lo pongo cuando obtengo una excepcion de las mencionadas, la calculadora se cae
        try:    
            if operacion not in ["1","2","3","4","5","6"]:    #Para cuando usuario dija opcion que no esta en el menú
                raise ValueError("Has ingresado un número de operación inválido. Por favor, elige una opción del menú.")
            if operacion == "6":
                print("Saliendo de la calculadora.")
                break
            
            if operacion == "5":
                numero_actual = borrar()
                print("Resultado ha sido borrado, el número actual es 0.")
            else:
                num2 = input("Ingrese un número: ")
                try:
                    num2 = float(num2)
                except ValueError:    #Para cuando el usuario ingresa algo que no es un número
                    raise ValueError("Entrada no válida para el número. Solo se permiten números")
                
                if operacion == "1":
                    numero_actual = sumar(numero_actual, num2)
                    print(f"Resultado de la suma es: {numero_actual}")
                elif operacion == "2":
                    numero_actual = restar(numero_actual, num2)
                    print(f"Resultado de la resta es: {numero_actual}")
                elif operacion == "3":
                    numero_actual = multiplicar(numero_actual, num2)
                    print(f"Resultado de la multiplicación es: {numero_actual}")
                elif operacion == "4":
                    numero_actual = dividir(numero_actual, num2)
                    print(f"Resultado de la división es: {numero_actual}")
                    
            
        except ValueError as e:
            print(f"Error: {e}")

        continuar = input("Quieres realizar otra operación? (s/n): ")  #relacion con el while true, siendo s = True
        if continuar.lower()!= "s":
            print("Saliendo de la calculadora.")
            break
        

if __name__ == "__main__":
    main()
