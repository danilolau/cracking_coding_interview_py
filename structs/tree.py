import random

class BinarySearchTree:
    class Node:
        def __init__(self,item) -> None:
            self.item = item
            self.left_child = None
            self.right_child = None
            self.parent = None

        def __repr__(self) -> str:
            return str(self.item)

    def __init__(self, root=None) -> None:
        self.root = self.Node(root)
    
    def add_node(self,item):
        node = self.Node(item)
        if self.root is None:
            self.root = node
        else:
            self.__add_node(self.root,node)
        
    def __add_node(self,parent,node):
        if node.item < parent.item:
            if parent.left_child is None:
                parent.left_child = node
                node.parent = parent
            else:
                self.__add_node(parent.left_child,node)
        else:
            if parent.right_child is None:
                parent.right_child = node
                node.parent = parent
            else:
                self.__add_node(parent.right_child,node)

    def min_node(self,node):
        if node.left_child is None:
            return node
        else:
            return self.min_node(node.left_child)
    
    def max_node(self,node):
        if node.right_child is None:
            return node
        else:
            return self.max_node(node.right_child)

    def __print_tree(self, node):
        if node is None:
            return "[ ]"
        else:
            left_str = self.__print_tree(node.left_child)
            right_str = self.__print_tree(node.right_child)
            return "{" + left_str + "-" + str(node) + "-" + right_str + "}"
        
    def __str__(self) -> str:
        return self.__print_tree(self.root)

tree = BinarySearchTree(500)

for i in range(20):
    item = random.randint(0,1000)
    tree.add_node(item)

print(tree)

