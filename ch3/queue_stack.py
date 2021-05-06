class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def push(self, node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def pop(self):
        data = None
        if self.first is not None:
            data = self.first
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
        return data

    def __repr__(self):
        nodes = []
        pointer = self.first
        nodes.append("-->")
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)

class Stack:
    def __init__(self):
        self.head = None

    def push(self,node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
    def pop(self):
        data = self.head
        if data is not None:
            self.head = self.head.next
            data.next = None
        return data

    def is_empty(self):
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty

    def __repr__(self):
        nodes = []
        pointer = self.head
        nodes.append("-->")
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)

