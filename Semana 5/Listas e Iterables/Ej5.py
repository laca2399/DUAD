

my_list = []
temporal = 0

for i in range (10):
    num = int(input("Ingrese un número: "))
    my_list.append(num)
    if num > temporal:
        temporal = num
    
print(f"{my_list}. El más alto fue {temporal}.")
