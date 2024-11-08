#1. Cree una estructura de objetos que asemeje una Queue.
#    1. Debe incluir los métodos de `enqueue` (para agregar nodos) y `dequeue` (para quitar nodos).
#    2. Debe incluir un método para hacer `print` de toda la estructura.
#    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    data: str  #stores value of node
    next: "Node"  #points the next node in the queue

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    head: Node  #First node of the queue, will be the first out (FIFO)

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head  #starts with the initial node

        while(current_node is not None):  #While there is a node
            print(current_node.data)  #print the value of that node
            current_node = current_node.next  #advances to the next node

    #Method let us add a new node at the end of the queue
    def enqueue(self, new_node):
        current_node = self.head  #starts in the initial node

        while current_node.next is not None:  #iterates until find the last node
            current_node = current_node.next

        current_node.next = new_node  #once is in the last node, adds the new node at the end of queue

    #Method to delete the first node of the queue, the self.head
    def dequeue(self):
        if self.head:  #If self.head is not none (queue no empty)
            self.head = self.head.next  #The new first will be the second




first_node = Node("Hola")
my_queue = Queue(first_node)
my_queue.print_structure()

second_node = Node("Mundo")
my_queue.enqueue(second_node)

third_node = Node("third")
my_queue.enqueue(third_node)

forth = Node("forth")
my_queue.enqueue(forth)

my_queue.print_structure()

print("DEQUEUE")
my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()


print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()