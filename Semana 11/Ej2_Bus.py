#2. Cree una clase de `Bus` con:
#    1. Un atributo de `max_passengers`.
#    2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). 
# Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#    3. Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person:
    def __init__ (self,name):
        self.name = name


class Bus:
    def __init__ (self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []  #To store instances of Person Class

    def add_passengers(self,person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f'{person.name} has gotten on the bus.')
        else:
            print('The bus is full. No more persons allowed.')

    def remove_passengers(self,person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person.name} has gotten off the bus.')
        else:
            print(f'{person.name} is not in the bus.')

person1 = Person("Mario")
person2 = Person ("Hellen")
person3 = Person("Andy")

my_bus = Bus(2)  #max_passengers allowed
my_bus.add_passengers(person1)
my_bus.add_passengers(person2)
my_bus.add_passengers(person3)

my_bus.remove_passengers(person2)

my_bus.remove_passengers(person2)