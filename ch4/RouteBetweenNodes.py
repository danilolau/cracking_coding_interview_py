import sys
import os
from structs.graph import Graph

import random

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

