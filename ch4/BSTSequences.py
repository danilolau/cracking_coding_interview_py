from structs.tree import BinarySearchTree
import random

def weave_lists(list_a: list,list_b: list):
    if not list_a:
        return [list_b]
    if not list_b:
        return [list_a]
    if not list_a and not list_b:
        return []

    prepend_a = list_a[0]
    prepend_b = list_b[0]
    weaved_list = []

    seqs_a = weave_lists(list_a[1:],list_b)
    seqs_b = weave_lists(list_a,list_b[1:])


    for elem in seqs_a:
        temp = [prepend_a]
        temp.extend(elem)
        weaved_list.append(temp)

    for elem in seqs_b:
        temp = [prepend_b]
        temp.extend(elem)
        weaved_list.append(temp)

    return weaved_list


def bst_sequences(node: BinarySearchTree.Node):
    if node is None:
        return []

    seq_left = bst_sequences(node.left_child)
    seq_right = bst_sequences(node.right_child)

    sequences = []

    if not seq_left and not seq_right:
        temp = [node]
        sequences.append(temp)
    elif not seq_left:
        for elem in seq_right:
            temp = [node]
            temp.extend(elem)
            sequences.append(temp)
    elif not seq_right:
        for elem in seq_left:
            temp = [node]
            temp.extend(elem)
            sequences.append(temp)
    else:
        for left in seq_left:
            for right in seq_right:
                weaved = weave_lists(left,right)
                for elem in weaved:
                    temp = [node]
                    temp.extend(elem)
                    sequences.append(temp)

    return sequences

ordered_list = random.choices(range(1000), k = 4)
#ordered_list.sort()
tree = BinarySearchTree()
#min_tree(ordered_list, tree)

for elem in ordered_list:
    tree.add_node(elem)

print(tree)
sequences = bst_sequences(tree.root)
print(sequences)
for seq in sequences:
    tree = BinarySearchTree()
    for elem in seq:
        tree.add_node(elem)
    print(tree)