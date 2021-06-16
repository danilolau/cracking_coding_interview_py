from ..structs.stack import Stack

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minStack = Stack()
    
    def push(self, item):
        super().push(item)
        if self.minStack.head is None:
            self.minStack.push(item)
        else:
            min_value = min(item,self.minStack.head.item)
            self.minStack.push(min_value)

    def pop(self):
        self.minStack.pop()
        return super().pop()

    def min(self):
        return self.minStack.head

min_stack = MinStack()
min_stack.push(10)
print(min_stack.min())
min_stack.push(8)
print(min_stack.min())
min_stack.push(12)
print(min_stack.min())
min_stack.push(16)
print(min_stack.min())
min_stack.push(4)
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
print(min_stack.min())




