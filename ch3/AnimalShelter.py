from ..structs.queue import Queue
import random

class AnimalShelter:
    def __init__(self):
        self.__dog_queue = Queue()
        self.__cat_queue = Queue()
        self.__seq = 0

    def enqueue(self,animal: str = "dog"):
        if animal.lower() == "dog":
            self.__dog_queue.enqueue(self.__seq)
            self.__seq += 1
        elif animal.lower() == "cat":
            self.__cat_queue.enqueue(self.__seq)
            self.__seq += 1

    def dequeue_dog(self):
        return self.__dog_queue.dequeue()

    def dequeue_cat(self):
        return self.__cat_queue.dequeue()

    def dequeue_any(self):
        data = None
        if self.__dog_queue.first.item < self.__cat_queue.first.item:
            data = self.__dog_queue.dequeue()
        else:
            data = self.__cat_queue.dequeue()
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


