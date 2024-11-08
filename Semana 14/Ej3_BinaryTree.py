class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  #left son
        self.right = None #right son  

class BinaryTree:
    def __init__(self):
        self.root = None  #Tree starts with empty root

    #Method to set the roof of the tree when there is no a root
    def set_root(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            print("The root is already set")


    #Method to insert a new node as left son of a current node    
    def insert_left(self, current_node, data):
        if current_node.left is None:  #Verifies if current node has already a left son
            current_node.left = Node(data)  #if None, new node will be the left son of current node
        else:                 
            #If not None, node already has a left son, in this case we need to add new node without deleting the current left son
            new_node = Node(data)  #creates new node
            new_node.left = current_node.left
            #the new node will be establish as the left son of the current node, and the node that was already there
            #will establish as the left son of the new node


            current_node.left = new_node #updates to point new node

    def insert_right(self, current_node, data):
        if current_node.right is None:  #Verifies if current node has already a right son
            current_node.right = Node(data)  #if None, new node will be the right son of current node
        else:  
            #If not None, node already has a right son, in this case we need to add new node without deleting the current right son
            new_node = Node(data) #creates  new node
            new_node.right = current_node.right
            #the new node will be establish as the right son of the current node, and the node that was already there
            #will establish as the right son of the new node

            current_node.right = new_node  #updates to point new node
    

    def print_structure(self, node):
        if node:
            self.print_structure(node.left) #Run the left subtree
            print(node.data)  #print value of current node
            self.print_structure(node.right)  #Run the right subtree


binarytree = BinaryTree()
binarytree.set_root("First")
binarytree.insert_left(binarytree.root, "1")
binarytree.insert_right(binarytree.root, "2")

binarytree.insert_left(binarytree.root, "3")
binarytree.insert_right(binarytree.root, "4")
binarytree.insert_left(binarytree.root, "5")
binarytree.insert_right(binarytree.root, "6")

binarytree.print_structure(binarytree.root)