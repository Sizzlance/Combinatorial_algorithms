def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        weight_matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            weight_matrix.append(row)
        source = int(f.readline())
        target = int(f.readline())
    return n, weight_matrix, source, target


def topological_sort(n, weight_matrix):
    visited = [False] * (n + 1)
    order = []

    def dfs(u):
        visited[u] = True
        for v in range(1, n + 1):
            if weight_matrix[u - 1][v - 1] != 32767 and not visited[v]:
                dfs(v)
        order.append(u)

    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u)

    return order[::-1]


def find_shortest_path_dag(n, weight_matrix, source, target):
    top_order = topological_sort(n, weight_matrix)

    dist = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    dist[source] = 0

    for u in top_order:
        for v in range(1, n + 1):
            if weight_matrix[u - 1][v - 1] != 32767:
                if dist[v] > dist[u] + weight_matrix[u - 1][v - 1]:
                    dist[v] = dist[u] + weight_matrix[u - 1][v - 1]
                    prev[v] = u

    if dist[target] == float('inf'):
        return None, None

    path = []
    u = target
    while u != -1:
        path.append(u)
        u = prev[u]
    path = path[::-1]

    return path, dist[target]


def write_output(filename, path, total_weight):
    with open(filename, 'w') as f:
        if path is None:
            f.write("N")
        else:
            f.write("Y\n")
            f.write(' '.join(map(str, path)) + '\n')
            f.write(str(total_weight))


if __name__ == "__main__":
    n, weight_matrix, source, target = read_input('in.txt')
    path, total_weight = find_shortest_path_dag(n, weight_matrix, source, target)
    write_output('out.txt', path, total_weight)