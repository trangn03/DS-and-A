class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
    
    # Append to empty linked list
    def append2(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    # Prepend node to empty linked list
    def prepend2(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
    
    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                return
            iterator = iterator.next

    def iterate(self):
        iterator = self.head
        while iterator:
            print(iterator.value + " ")
            iterator = iterator.next
    
    # Adding at the end O(1)
    # Insert at the beginning O(1)
    # Delete at the beginning is O(1)
    # Deleting after a node is O(n) 
    # Traversing is O(n)
    # Searching is O(n)
    # Insearting after a node is O(n) because we need to find the node until we have the node that we want
