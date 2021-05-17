from structs.tree import BinarySearchTree
from .MinimalTree import min_tree
import random


def check_balance(node):
    if node is None:
        return (True,0)

    b_left, h_left = check_balance(node.left_child)
    b_right,h_right = check_balance(node.right_child)

    diff = abs(h_right - h_left)
    height = max(h_left,h_right) + 1
    balanced = b_left and b_right and (diff < 2)
    
    return (balanced,height)


ordered_list = random.choices(range(1000), k = 7)
#ordered_list.sort()
tree = BinarySearchTree()
#min_tree(ordered_list, tree)

for elem in ordered_list:
    tree.add_node(elem)

print(tree)
print(check_balance(tree.root))