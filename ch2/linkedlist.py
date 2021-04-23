class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        
    def append_to_tail(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def append_list_to_tail(self,values):
        for value in values:
            self.append_to_tail(Node(value))
        
    def remove_by_val(self,value):
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        pointer = self.head
        
        while pointer.next != self.tail:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
                return True
            pointer = pointer.next
            
        if self.tail.value == value:
            self.tail = pointer
            self.tail.next = None
            return True
        
        return False
        
    def __repr__(self):
        nodes = []
        pointer = self.head
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)
    
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        
    def append_to_tail(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
    def append_list_to_tail(self,values):
        for value in values:
            self.append_to_tail(Node(value))
        
    def remove_by_ref(self,node):
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        return True
                
    def remove_by_val(self,value):        
        pointer = self.head
        while pointer is not None:
            if value == pointer.value:
                return self.remove_by_ref(pointer)
            pointer = pointer.next
        
        return False
    
    def __repr__(self):
        nodes = []
        pointer = self.head
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)
                
            
        
        
        
            
        
        
        
        
        