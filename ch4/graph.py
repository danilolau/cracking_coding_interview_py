from std_queue import Queue
import random

class Graph:
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []

        def add_child(self,node):
            self.children.append(node)

        def __hash__(self):
            return hash(self.value)

        def __repr__(self):
            return str(self.value)

    def __init__(self):
        self.__table = {}
        self.__cost = {}
        self.__root = None

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
        self.__cost[(a,b)] = cost

    def set_root(self,value):
        node = self.__table.get(value,None)
        if node is None:
            node = self.Node(value)
            self.__table[value] = node
        self.__root = node

    def get_root(self):
        return self.__root

    def set_node(self,value):
        node = self.__table.get(value,None)
        if node is None:
            node = self.Node(value)
            self.__table[value] = node

    def get_node(self,value):
        return self.__table.get(value,None)

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

    def search_bfs_bi(self,a,b):
        if a == b:
            return (True,str(a) + "=" + str(b))
        dict_path_a = {}
        dict_path_b = {}
        queue_a = Queue()
        queue_b = Queue()
        queue_a.push(self.__table[a])
        queue_b.push(self.__table[b])
        dict_path_a[a] = str(a) + "->"
        dict_path_b[b] = "<-" + str(b)
        while(not (queue_a.is_empty() and queue_b.is_empty())):
            node_a = queue_a.pop()
            node_b = queue_b.pop()
            if node_a is not None:
                for c in node_a.children:
                    path_a = dict_path_a.get(c.value,None)
                    if path_a is None:
                        dict_path_a[c.value] = dict_path_a[node_a.value] + str(c) + "->"
                        visited = dict_path_b.get(c.value,None)
                        if visited is not None:
                            path = dict_path_a[c.value] + visited
                            return (True,path)
                        queue_a.push(c)
            if node_b is not None:
                for c in node_b.children:
                    path_b = dict_path_b.get(c.value,None)
                    if path_b is None:
                        dict_path_b[c.value] = "<-" + str(c) + dict_path_b[node_b.value]
                        visited = dict_path_a.get(c.value,None)
                        if visited is not None:
                            path = visited + dict_path_b[c.value]
                            return (True,path)
                        queue_b.push(c)
        return (False,"")


    def __repr__(self):
        nodes = []
        for item in self.__table.values():
            nodes.append(str(item) + " --> " + str(item.children) + "\n")
        return "".join(nodes)

graph_test = Graph()
graph_test.add_path(0,1,1)
graph_test.add_path(0,4,1)
graph_test.add_path(0,5,1)
graph_test.add_path(1,4,1)
graph_test.add_path(1,3,1)
graph_test.add_path(3,2,1)
graph_test.add_path(3,4,1)
graph_test.add_path(2,1,1)

for i in range(30):
    a = random.choice([0,1,2,3,4,5])
    b = random.choice([0,1,2,3,4,5])
    print("Search path from {} to {}".format(a,b))
    print(graph_test.search_bfs(a,b))
    print(graph_test.search_dfs(a,b))

