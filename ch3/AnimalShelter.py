from queue_stack import Queue, Node
import random

class AnimalShelter:
    def __init__(self):
        self.__dog_queue = Queue()
        self.__cat_queue = Queue()
        self.__seq = 0

    def enqueue(self,animal = "dog"):
        if animal.lower() == "dog":
            self.__dog_queue.push(Node(self.__seq))
            self.__seq += 1
        elif animal.lower() == "cat":
            self.__cat_queue.push(Node(self.__seq))
            self.__seq += 1

    def dequeue_dog(self):
        return self.__dog_queue.pop()

    def dequeue_cat(self):
        return self.__cat_queue.pop()

    def dequeue_any(self):
        data = None
        if self.__dog_queue.first.value < self.__cat_queue.first.value:
            data = self.__dog_queue.pop()
        else:
            data = self.__cat_queue.pop()
        return data

    def __repr__(self):
        return "Cat queue: " + "\n" + str(self.__cat_queue) + "\n" + "Dog queue: " + "\n" + str(self.__dog_queue) + "\n"

shelter = AnimalShelter()

for i in range(15):
    animal = random.choice(['dog','cat'])
    shelter.enqueue(animal)
    print("adding to the shelter: {}".format(animal))
    print(shelter)

for i in range(15):
    animal = random.choice(['dog','cat','any'])
    data = None
    if animal == 'dog':
        data = shelter.dequeue_dog()
    elif animal == 'cat':
        data = shelter.dequeue_cat()
    else:
        data = shelter.dequeue_any()

    print("Dequeueing {}: {}".format(animal, data))
    print(shelter)


