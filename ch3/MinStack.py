from queue_stack import Node, Stack

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minStack = Stack()
    
    def push(self, node):
        super().push(node)
        if self.minStack.head is None:
            self.minStack.push(Node(node.value))
        else:
            min_value = min(node.value,self.minStack.head.value)
            self.minStack.push(Node(min_value))

    def pop(self):
        self.minStack.pop()
        return super().pop()

    def min(self):
        return self.minStack.head

min_stack = MinStack()
min_stack.push(Node(10))
print(min_stack.min())
min_stack.push(Node(8))
print(min_stack.min())
min_stack.push(Node(12))
print(min_stack.min())
min_stack.push(Node(16))
print(min_stack.min())
min_stack.push(Node(4))
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())




