from queue_stack import Node, Stack
import random

class QueueViaStack:
    def __init__(self):
        self.__pop_stack = Stack()
        self.__push_stack = Stack()

    def push(self,node):
        self.__push_stack.push(node)

    def pop(self):
        if self.__pop_stack.is_empty():
            while self.__push_stack.is_empty() == False:
                item = self.__push_stack.pop()
                self.__pop_stack.push(item)
        return self.__pop_stack.pop()

    def __repr__(self):
        return  str(self.__push_stack) + "\n" + str(self.__pop_stack) + "\n"

queue_via_stack = QueueViaStack()

for i in range(15):
    value = random.randint(1,1000)
    queue_via_stack.push(Node(value))
    print("adding to the queue: {}".format(value))
    print(queue_via_stack)

for i in range(10):
    data = queue_via_stack.pop()
    print("removing from the queue {}".format(data))
    print(queue_via_stack)

for i in range(15):
    value = random.randint(1,1000)
    queue_via_stack.push(Node(value))
    print("adding the plate: {}".format(value))
    print(queue_via_stack)

for i in range(20):
    data = queue_via_stack.pop()
    print("removing the plate {}".format(data))
    print(queue_via_stack)