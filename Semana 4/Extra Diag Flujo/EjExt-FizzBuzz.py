num = int(input("Ingrese un número: "))
if(num%5==0 and num%3==0):
    print("FizzBuzz")
elif (num%5==0):
    print("Buzz")
elif(num%3==0):
    print("Fizz")
else:
    print("No es divisible ni por 5 ni por 3")