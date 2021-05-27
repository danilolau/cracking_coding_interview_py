from structs.tree import BinarySearchTree
import random

def check_path(node: BinarySearchTree.Node, kth_sums: list, paths: list, sum: int):
    if node is None:
        return None
    
    for i, _ in enumerate(kth_sums):
        kth_sums[i] += node.item
        if kth_sums[i] == sum:
            kth = len(kth_sums) - i
            paths.append((node,kth))
    kth_sums.append(node.item)
    if node.item == sum:
        paths.append((node,0))
    check_path(node.left_child,kth_sums.copy(),paths,sum)
    check_path(node.right_child,kth_sums.copy(),paths,sum)

def sum_paths(tree: BinarySearchTree, sum: int):
    paths = []
    kth_sums = []
    check_path(tree.root,kth_sums.copy(),paths,sum)
    return paths

def gen_sums(tree: BinarySearchTree):
    node = tree.get_random_node()
    pointer: BinarySearchTree.Node = node
    values = []
    while pointer is not None:
        values.append(pointer.item)
        pointer = pointer.parent

    count = random.choice(range(len(values)))
    sum = 0

    while count >= 0:
        sum += values[count]
        count -= 1

    return sum

ordered_list = random.choices(range(-10,10), k = 15)
tree = BinarySearchTree()

for elem in ordered_list:
    tree.add_node(elem)

print(tree)
sum = gen_sums(tree)
print("for sum {}, this is the path:".format(sum))
paths = sum_paths(tree,sum)
print(paths)
checks = []
for path in paths:
    pointer = path[0]
    count = path[1]
    check = 0
    while count >= 0:
        check += pointer.item
        pointer = pointer.parent
        count -= 1
    checks.append(check)
print(checks)










