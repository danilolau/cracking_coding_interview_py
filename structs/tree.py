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

        def __eq__(self, other) -> bool:
            return self.item == other.item

        def __hash__(self) -> int:
            return hash(self.item)

    def __init__(self) -> None:
        self.root = None
    
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

    def add_random(self, item):
        child = self.Node(item)
        if self.root is None:
            self.root = child
        else:
            self.__add_random(self.root,child)

    def __add_random(self, node: Node, child: Node):
        if node.left_child is None:
            node.left_child = child
            child.parent = node
        elif node.right_child is None:
            node.right_child = child
            child = node
        else:
            c = random.choice([0,1])
            if c == 0:
                self.__add_random(node.left_child,child)
            else:
                self.__add_random(node.right_child,child)

    def find(self, item):
        pass

    def successor(self, node: Node):
        if node.right_child is not None:
            return self.min_node(node.right_child)
        elif node.left_child is not None:
            return self.max_node(node.left_child)
        else:
            return None
        

    def min_node(self,node: Node):
        if node.left_child is None:
            return node
        else:
            return self.min_node(node.left_child)
    
    def max_node(self,node: Node):
        if node.right_child is None:
            return node
        else:
            return self.max_node(node.right_child)

    def print_tree(self, node, level):
        if node is None:
            return "[ ]"
        else:
            left_str = self.print_tree(node.left_child, level + 1)
            right_str = self.print_tree(node.right_child, level + 1)
            node_str = str(node) + "\n" + level*"\t" + left_str + "\n" + level*"\t" + right_str
            return node_str
        
    def __str__(self) -> str:
        return self.print_tree(self.root,1)


