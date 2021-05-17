from structs.tree import BinarySearchTree
import math
import random

def min_tree(ordered_list: list, tree: BinarySearchTree):
    middle = math.floor(len(ordered_list)/2)
    tree.add_node(ordered_list[middle])
    if middle > 0:
        min_tree(ordered_list[:middle],tree)
    if len(ordered_list) > 2:
        min_tree(ordered_list[middle+1:],tree)



ordered_list = random.choices(range(1000), k = 31)
ordered_list.sort()
tree = BinarySearchTree()
min_tree(ordered_list, tree)
print(tree)




