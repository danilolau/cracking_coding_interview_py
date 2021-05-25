from structs.tree import BinarySearchTree
import random

def random_node(tree: BinarySearchTree):
    pass


ordered_list = random.choices(range(1000), k = 15)
#ordered_list.sort()
tree = BinarySearchTree()
#min_tree(ordered_list, tree)

for elem in ordered_list:
    tree.add_node(elem)

elem = random.choice(ordered_list)

print(tree)
print("length: {}".format(tree.length))
print("remove the element: {}".format(elem))
tree.remove(elem)
print("length: {}".format(tree.length))
print(tree)

