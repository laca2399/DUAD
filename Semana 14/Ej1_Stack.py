class Node:
    data: str   #stores the value of the node
    next: "Node"  #points the next node

    def __init__(self, data):
        self.data = data
        self.next = None  #indicates that there is not a next node when a node is created

class Stack:

    def __init__(self):
        self.top = None  #Top is the top node of the stack and the last added, so will be the first out
        #If top is none, then stack is empty

    def print_structure(self):  
        current_node = self.top  #Starts from the the top of the stack to the bottom

        while(current_node is not None):  #Iterates while not note
            print(current_node.data)  #each iteration prints value of current node
            current_node = current_node.next  #moves current to the next

    #Method to add a new node at the top of the stack
    def push (self, new_node):
        new_node.next = self.top  #The next of the new node points to the node that is actually at the top
        self.top = new_node  #converts the new node in the top

    #Method to delete top node from the stack
    def pop (self):
        if self.top is None:  #Checks if stack is empty
            print("Stack is empty")
            return None
        
        popped_node = self.top  #If stack not empty, saves the top node in popped_node
        self.top = self.top.next  #updates self.top to point to the next
        return popped_node.data  #allows the user know that this elements was deleted of stack
    
stack = Stack()

stack.push(Node("Hello"))
stack.push(Node("I am first"))
stack.push(Node("I am second"))

print("Stack after adding nodes")
stack.print_structure()

print("Pop")
stack.pop()
stack.print_structure()
        