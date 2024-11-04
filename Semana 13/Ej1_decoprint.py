#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def parameters_returns (func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")

        return result
    return wrapper

@parameters_returns
def show_info (name, surname, age = None, city = None):
    return f"{name} {surname} is {age} years old and live in {city}."

show_info("Hernan", "Fallas", age=50, city="Paris")

