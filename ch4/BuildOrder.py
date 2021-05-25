from structs.graph import Graph

def build_order(deps: Graph):
    is_possible = True
    projects = []
    while is_possible and not deps.is_empty():
        is_possible = False
        to_remove = []
        for elem in deps.get_table():
            if not deps.get_node(elem).parents:
                is_possible = True
                projects.append(elem)
                to_remove.append(elem)
        for elem in to_remove:
            deps.remove_node(elem)

    return (is_possible,projects)

graph_test = Graph()
graph_test.add_path('a','d',1)
graph_test.add_path('f','b',1)
graph_test.add_path('b','d',1)
graph_test.add_path('f','a',1)
graph_test.add_path('d','c',1)
graph_test.add_path('c','b',1)
graph_test.set_node('e')

print(build_order(graph_test))





    