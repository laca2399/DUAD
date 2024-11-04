#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore 
# son números, y arroje una excepción de no ser así.

def check_if_numbers(func):
    def wrapper(*args):
        print("Checking if all parameters are numbers")
        for arg in args:
            try:
                num = float(arg)
            except  (ValueError, TypeError):
                raise TypeError("All the arguments must be numbers")
        
        return func(*args)
    return wrapper

@check_if_numbers
def multiply(a, b):
    return a * b

print(multiply(7,8))

print(multiply(7,"Hello World"))

