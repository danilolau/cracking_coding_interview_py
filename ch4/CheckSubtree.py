from ch4.SumPaths import check_path
from structs.tree import BinarySearchTree
import random

def cmp_subtree(node_a: BinarySearchTree.Node, node_b: BinarySearchTree.Node):
    
    cmp = False
    
    if node_a is None:
        return cmp

    if node_a == node_b:
        cmp = True

    if node_b.left_child is not None:
        cmp = cmp and cmp_subtree(node_a.left_child, node_b.left_child)
    
    if node_b.right_child is not None:
        cmp = cmp and cmp_subtree(node_a.right_child, node_b.right_child)

    return cmp

def check_subtree(tree: BinarySearchTree, subtree: BinarySearchTree):
    
    pointer = tree.root
    check = False

    while pointer is not None:
        if subtree.root == pointer:
            check = cmp_subtree(pointer, subtree.root)
            break
        elif subtree.root < pointer:
            pointer = pointer.left_child
        else:
            pointer = pointer.right_child

    return check


ordered_list = random.choices(range(1000), k = 100)
tree = BinarySearchTree()

for elem in ordered_list:
    tree.add_node(elem)

node = tree.get_random_node()

subtree = BinarySearchTree()

subtree.add_node(node.item)

if node.left_child is not None:
    subtree.add_node(node.left_child.item)

if node.right_child is not None:
    subtree.add_node(node.right_child.item)
    if node.right_child.left_child is not None:
        subtree.add_node(node.right_child.left_child.item)

#uncomment the line below if you would like to test the false hypothesis:
#subtree.add_node(random.choice(range(1000)))


print("This is the tree:")
print(tree)
print("This is the subtree: ")
print(subtree)
print("The subtree is really a subtree of tree? {}:".format(check_subtree(tree,subtree)))





