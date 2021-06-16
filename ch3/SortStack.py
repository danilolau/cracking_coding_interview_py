from .queue_stack import Stack, Node
import random

def sort_stack(stack = Stack()):
    temp_stack = Stack()
    while not stack.is_empty():
        item = stack.pop()
        if temp_stack.is_empty():
            temp_stack.push(item)
        else:
            counter = 0
            while not temp_stack.is_empty() and item.value < temp_stack.head.value:
                stack.push(temp_stack.pop())
                counter += 1
            temp_stack.push(item)
            while(counter > 0):
                temp_stack.push(stack.pop())
                counter -= 1
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

stack = Stack()

for i in range(30):
    value = random.randint(1,1000)
    stack.push(Node(value))
    print("adding to the stack: {}".format(value))
    print(stack)

sort_stack(stack)

print("Sorted Stack:")
print(stack)