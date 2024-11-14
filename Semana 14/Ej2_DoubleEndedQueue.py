class Node:
    def __init__ (self,data):
        self.data = data #stores value of Node
        self.next = None #Points next (to the right) that there is currently None as there is no Node
        self.prev = None  #Points prev (to the left) that there is currently None as there is no Node

class DoubEnd_Queue:
    def __init__(self):
        self.head = None  #Points to the first node (Left side)
        self.tail= None  #Points to the last node (right side)

    def print_structure(self):
        current_node = self.head  
        print("Double Ended Queue Elements:")
        while current_node:  #Iterates from head to tail
            print(current_node.data)  #print data of each node
            current_node = current_node.next  #advances to next node
        print()

    def is_empty(self):
        return self.head is None  #returns True if structure is empty
    
    #Method to add a new node at the beginning (left side / head)
    def push_left(self,data):
        new_node = Node(data)  #creates a new node

        if self.is_empty():  #If is empty
            self.head = self.tail = new_node  #head and tail will point to the new node
        else:
            new_node.next = self.head  #establish in head
            self.head.prev = new_node  #updates to point new node
            self.head = new_node  #updates to point new node

    #Method to add a new node at the end (Right side / tail)
    def push_right (self,data):
        new_node = Node(data)  #creates a new node

        if self.is_empty():  #If is empty
            self.head = self.tail = new_node  #head and tail will point to the new node
        else:
            new_node.prev = self.tail  #establish in tail
            self.tail.next = new_node  #updates to point new node
            self.tail = new_node  #updates to point new node
    

    #Method to delete the node from the beginning (left side / head)
    def pop_left(self):
        if self.is_empty():
            print ("Double Ended Queue is empty")
            return None
        
        removed_data = self.head.data  #save the data of the node that will be deleted
        self.head = self.head.next  #The new head is the node that points to the next

        if self.head is None:  #If after updating head is None, then is empty
            self.tail = None
        else:
            self.head.prev = None  #If structure not empty, deletes the reference to the deleted node
        
        return removed_data
    
    #Method to delete the node from the end (Right side / tail)
    def pop_right(self):
        if self.is_empty():
            print ("Double Ended Queue is empty")
            return None
        
        removed_data = self.tail.data #save the data of the node that will be deleted
        self.tail = self.tail.prev #The new tail is the node that points to the prev

        if self.tail is None:  #If after updating tail is None, then is empty structure
            self.head = None
        else:
            self.tail.next = None  #If structure not empty, deletes the reference to the deleted node
        
        return removed_data
    
deque = DoubEnd_Queue()
deque.push_left("First")
deque.push_right("Second")
deque.push_left("Third")
deque.push_right("Fourth")

deque.print_structure()

print ("Deleting from left")
deque.pop_left()
deque.print_structure()

print ("Deleting from right")
deque.pop_right()
deque.print_structure()

