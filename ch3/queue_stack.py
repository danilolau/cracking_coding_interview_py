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
    
    def add(self, node):
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
        while pointer is not None:
            nodes.append(str(pointer))
            nodes.append("-->")
            pointer = pointer.next
        return "".join(nodes)

