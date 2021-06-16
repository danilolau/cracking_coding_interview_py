from ..structs.tree import BinarySearchTree
import random


ordered_list = random.choices(range(1000), k = 100)
tree = BinarySearchTree()

for elem in ordered_list:
    tree.add_node(elem)

print(tree)

while tree.root is not None:
    elem = tree.get_random_node()
    print("length: {}".format(tree.length))
    print("remove the element: {}".format(elem))
    tree.remove(elem.item)
    print("length: {}".format(tree.length))
    print(tree)

