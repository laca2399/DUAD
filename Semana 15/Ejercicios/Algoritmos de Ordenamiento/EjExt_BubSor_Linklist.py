#Implemente un bubble_sort que funcione para @Linked Lists.

class Node:
    data: str   #stores value of the node
    next: "Node"  #points the next node of the list

    def __init__(self, data):
        self.data = data
        self.next = None  #this indicates that node does not points to another node when created

class LinkedList:
    head: Node  #points to the first node of the list

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head  #the initial node

        while(current_node is not None):  #For each iteration 
            print(current_node.data, end=" , " if current_node.next else "\n")  # 1 , 2 , 3 , 4 , 5 method of print
            current_node = current_node.next  #advances to the next node of the list

    def bubble_sort(self):
        end = None  #Use to mark the last node that is already in correct position
        while end != self.head:  #loop until end equals first node
            exchange = False  #initialize exchange in False
            current = self.head #initialize current pointing to first node of list
            while current.next != end:  #internal loop from the beginning until the node mark by end
                next_node = current.next  #Assign to next_node, the next node to current
                print(f'-- Comparing: {current.data} y {next_node.data}')
                if current.data > next_node.data:  #if data of current node is bigger than data of next node
                    current.data, next_node.data = next_node.data, current.data  #switch places
                    exchange = True  #As there was an exchange, it is assigned a True value
                    print(f'   -> Exchange made: {current.data} <-> {next_node.data}')
                current = next_node  #moves the pointer of current to the next_node

            if not exchange:  #When exchange is false at end of iteration, means that list is sorted
                break
        end = current  #mark the current node as end as it is in correct position

#First we give values to the linked list:
first_node = Node (5)
second_node = Node(10)
first_node.next = second_node
third_node = Node(3)
second_node.next = third_node
fourth_node = Node(32)
third_node.next = fourth_node
fifth_node = Node(1)
fourth_node.next = fifth_node

structure = LinkedList(first_node)  #establish where the linked list starts or self.head
print("Linked List before bubble sort:")
structure.print_structure()

structure.bubble_sort()
print("Linked List after bubble sort:")
structure.print_structure()