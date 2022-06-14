class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

 
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)


class LinkedListExample:
  def __init__(self, value): 
    """
    Initializes the new linked list and also creates a new Node.
    (Self parameter) This is a method inside of a class instead of a regular function. 
    (Value parameter) This is the value that will be passed down to our new node.
    """
  # Creates a new Node and adds the Node to the end  
  def append(self, value):           
  def prepend(self, value):           
  def insert(self, index, value):           
               
