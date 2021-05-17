from structs.linkedlist import LinkedList
from structs.tree import BinarySearchTree
import random

def list_of_depths(node, depths,level):
    
    if level < len(depths):
        depths[level].append(node)
    else:
        depths.append(LinkedList())
        depths[level].append(node)

    if node.left_child is not None:
        list_of_depths(node.left_child,depths,level+1)
    
    if node.right_child is not None:
        list_of_depths(node.right_child,depths,level+1)

depths = []
tree = BinarySearchTree()
random_list = random.choices(range(1000), k = 31)
for item in random_list:
    tree.add_node(item)

list_of_depths(tree.root,depths,0)

print("tree in his format: ")

print(tree)

print("Now a linked list by level: ")

for llist in depths:
    print(llist)