from collections import deque

def build_a_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        initial_graph = {}
        for i in range(1, n + 1):
            neighbors = list(map(int, f.readline().split()))
            initial_graph[i] = neighbors[:-1]
    return initial_graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    parent = {}
    cycle = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    parent[neighbor] = node
                elif neighbor in visited and parent.get(node) != neighbor:
                    cycle.append(neighbor)
                    cycle.append(node)
                    current = node
                    while current in parent and parent[current] != neighbor:
                        current = parent[current]
                        cycle.append(current)
                    cycle.append(neighbor)
                    return set(cycle)
    return None


def main():
    graph = build_a_graph('in.txt')
    if bfs(graph, 1) is None:
        with open('out.txt', 'w') as f:
            f.write('A\n')
    else:
        with open('out.txt', 'w') as f:
            f.write('N\n')
            f.write(" ".join(map(str, sorted(bfs(graph, 1)))) + "\n")
if __name__ == "__main__":
    main()
