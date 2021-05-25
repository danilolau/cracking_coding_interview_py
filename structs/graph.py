import random
from .queue import Queue

class Graph:
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []
            self.parents = []

        def add_child(self,node):
            self.children.append(node)

        def add_parent(self,node):
            self.parents.append(node)

        def __eq__(self, other: object) -> bool:
            return self.value == other.value

        def __hash__(self):
            return hash(self.value)

        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self.__table = {}
        self.__cost = {}
        self.__root = None

    def is_empty(self):
        return len(self.__table)==0

    def add_path(self,a, b, cost):
        node_a = self.__table.get(a,None)
        node_b = self.__table.get(b,None)
        if node_a is None:
            node_a = self.Node(a)
            self.__table[a] = node_a
        if node_b is None:
            node_b = self.Node(b)
            self.__table[b] = node_b
        node_a.add_child(node_b)
        node_b.add_parent(node_a)
        self.__cost[(a,b)] = cost

    def remove_node(self,value):
        node = self.get_node(value)
        if node is not None:
            for child in node.children:
                child.parents.remove(node)
            for parent in node.parents:
                parent.children.remove(node)
            node.children = []
            node.parents = []
            self.__table.pop(value)

    def set_node(self,value):
        node = self.__table.get(value,None)
        if node is None:
            node = self.Node(value)
            self.__table[value] = node

    def get_node(self,value) -> Node:
        return self.__table.get(value,None)

    def get_table(self):
        return self.__table

    def search_dfs(self,a,b):
        node = self.get_node(a)
        path = []
        marked = {}
        found = self.__dfs(node,b,path,marked)
        path.reverse()
        return (found,path)
        
    def __dfs(self,node,target,path,marked):
        if node.value == target:
            path.append(node)
            return True
        marked[node.value] = True
        for child in node.children:
            if not marked.get(child.value,False):
                r = self.__dfs(child,target,path,marked)
                if r:
                    path.append(node)
                    return True
        return False

    def search_bfs(self,a,b):
        if a == b:
            return (True, str(a) + "=" + str(b))
        dict_path = {}
        queue = Queue()
        queue.push(self.get_node(a))
        dict_path[a] = str(a) + "->"
        while not queue.is_empty():
            node = queue.pop()
            for c in node.children:
                path = dict_path.get(c.value,None)
                if path is None:
                    dict_path[c.value] = dict_path[node.value] + str(c) + "->"
                    if c.value == b:
                        return (True,dict_path[c.value])
                    queue.push(c)
        return (False,"")

    def __repr__(self):
        nodes = []
        for item in self.__table.values():
            nodes.append(str(item) + " --> " + str(item.children) + "\n")
        return "".join(nodes)


