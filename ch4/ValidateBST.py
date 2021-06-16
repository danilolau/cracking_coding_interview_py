from ..structs.tree import BinarySearchTree
import random

def validate_bst(node):
    reference = node.item
    is_bst = True

    if node.right_child is None:
        min_right, max_right, is_right_bst = reference,reference,True
    else:
        min_right, max_right, is_right_bst = validate_bst(node.right_child)
    
    if node.left_child is None:
        min_left, max_left, is_left_bst = reference,reference,True
    else:
        min_left, max_left, is_left_bst = validate_bst(node.left_child)


    if min_right < reference or max_left > reference:
        is_bst = False

    is_bst = is_bst and is_right_bst and is_left_bst

    min_value = min(reference,min_right,min_left)
    max_value = max(reference,max_right,max_left)

    return min_value, max_value, is_bst


ordered_list = random.choices(range(1000), k = 7)
#ordered_list.sort()
tree = BinarySearchTree()
#min_tree(ordered_list, tree)

for elem in ordered_list:
    c = random.choice([0,1])
    if c == 0:
        tree.add_random(elem)
    else:
        tree.add_node(elem)

print(tree)
print(validate_bst(tree.root))