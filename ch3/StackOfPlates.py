from queue_stack import Stack, Node
import random

class SetOfStacks:
    def __init__(self, threshold):
        self.__set = []
        self.__len = []
        self.__current = -1
        self.threshold = threshold

    def __add_new_stack(self, node):
            new_stack = Stack()
            new_stack.push(node)
            self.__set.append(new_stack)
            self.__len.append(1)
            self.__current += 1

    def push(self, node):
        if len(self.__set) == 0:
            self.__add_new_stack(node)
        elif self.__len[self.__current] == self.threshold:
            self.__add_new_stack(node)
        else:
            self.__set[self.__current].push(node)
            self.__len[self.__current] += 1

    def pop(self):
        data = None
        if len(self.__len) > 0:
            data = self.__set[self.__current].pop()
            self.__len[self.__current] -= 1
            if self.__len[self.__current] == 0:
                self.__len.pop(self.__current)
                self.__set.pop(self.__current)
                self.__current -= 1
        return data

    def pop_at(self, index):
        data = None
        if index <= self.__current and index >= 0:
            data = self.__set[index].pop()
            self.__len[index] -= 1
            if self.__len[index] == 0:
                self.__set.pop(index)
                self.__len.pop(index)
                self.__current -= 1
        return data

    def __repr__(self):
        plates = []
        for count, stack in enumerate(self.__set):
            plates.append('Stack of plates number: {} \n'.format(count))
            plates.append(str(stack) + '\n')
        return "".join(plates)

set_of_stacks = SetOfStacks(4)

for i in range(15):
    value = random.randint(1,1000)
    set_of_stacks.push(Node(value))
    print("adding the plate: {}".format(value))
    print(set_of_stacks)

for i in range(16):
    data = set_of_stacks.pop()
    print("removing the plate {}".format(data))
    print(set_of_stacks)

for i in range(15):
    value = random.randint(1,1000)
    set_of_stacks.push(Node(value))
    print("adding the plate: {}".format(value))
    print(set_of_stacks)

for i in range (15):
    #index = random.randint(0,4)
    index = 1
    data = set_of_stacks.pop_at(index)
    print("removing the plate {} from the stack {}".format(data,index))
    print(set_of_stacks)


