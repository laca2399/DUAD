list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

persona = {}

for i in range(len(list_a)):
    persona[list_a[i]]= list_b[i] 

print(persona)