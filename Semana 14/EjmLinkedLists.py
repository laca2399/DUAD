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
            print(current_node.data)  #print the data of the current node
            current_node = current_node.next  #advances to the next node of the list
        
first_node = Node ("Hello")
second_node = Node("I am first")
first_node.next = second_node
third_node = Node("I am second")
second_node.next = third_node

structure = LinkedList(first_node)
structure.print_structure()

#It will print until the third node, because the third node does not have a next. 