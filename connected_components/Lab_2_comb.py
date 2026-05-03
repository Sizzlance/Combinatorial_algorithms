def build_a_graph(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        initial_graph = {}

        for i in range(1, n + 1):
            line = list(map(int, file.readline().split()))
            neighbors = []
            for j in range(n):
                if line[j] == 1:
                    neighbors.append(j + 1)
                initial_graph[i] = neighbors
    return initial_graph

def dfs(graph, start, visited, component):
    visited.add(start)
    component.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def find_comp(graph):
    visited = set()
    components = []
    for vertex in sorted(graph.keys()):
        if vertex not in visited:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(sorted(component))
    return components

if __name__ == "__main__":
    init_graph = build_a_graph('in.txt')
    init_components = find_comp(init_graph)
    with open('out.txt', 'w') as f:
        f.write(str(len(init_components)) + '\n')
        for comp in init_components:
            f.write(' '.join(map(str, comp)) + '\n')