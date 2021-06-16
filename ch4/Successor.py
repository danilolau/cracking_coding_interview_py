import random
from ..structs.tree import BinarySearchTree

ordered_list = random.choices(range(1000), k = 31)
#ordered_list.sort()
tree = BinarySearchTree()
#min_tree(ordered_list, tree)

for elem in ordered_list:
    tree.add_node(elem)

print(tree)
print(tree.successor(tree.root.left_child))