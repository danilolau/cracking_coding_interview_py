import random
from ..structs.tree import BinarySearchTree

def random_at_depth(tree: BinarySearchTree, depth: int):
    if depth < 0:
        return None

    level = 0
    pointer = tree.root

    while level < depth and pointer is not None:
        rand = random.choice([False,True])
        if rand:
            pointer = pointer.left_child
        else:
            pointer = pointer.right_child
        level += 1

    return (pointer, level)

def first_common_ancestor(node_a,depth_a,node_b,depth_b):
    diff = depth_a - depth_b

    if node_a is None or node_b is None:
        return None

    while diff < 0:
        node_b = node_b.parent
        diff += 1

    while diff > 0:
        node_a = node_a.parent
        diff -= 1

    while node_b.parent is not None and node_b != node_a:
        node_a = node_a.parent
        node_b = node_b.parent

    return node_b

ordered_list = random.choices(range(1000), k = 64)
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

node_a, depth_a = random_at_depth(tree,5)
node_b, depth_b = random_at_depth(tree,3)

print((node_a,depth_a))
print((node_b,depth_b))
print(first_common_ancestor(node_a,depth_a,node_b,depth_b))