from collections import deque


def build_graph_from_matrix(filename):
    with (open(filename, 'r') as file):
        n = int(file.readline().strip())
        capacity_matrix = []

        for i in range(n):
            line = file.readline()
            if not line:
                break

            row = list(map(int, line.split()))
            capacity_matrix.append(row)

        start = int(file.readline().strip())
        finish = int(file.readline().strip())

        return capacity_matrix, start, finish, n


def bfs(capacity, flow, parent, s, t):
    num_vertices = len(capacity)
    visited = [False] * num_vertices
    queue = deque([s])
    visited[s] = True
    parent[s] = -1

    while queue:
        current = queue.popleft()

        for neighbor in range(num_vertices):
            # Можем пройти только если есть свободная пропускная способность
            residual_capacity = capacity[current][neighbor] - flow[current][neighbor]
            if not visited[neighbor] and residual_capacity > 0:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor == t:
                    return True

    return False


def ford_fulkerson(capacity, source, target):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0

    while bfs(capacity, flow, parent, source, target):
        path_flow = float('inf')
        v = target
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u

        v = target

        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow
    return flow, max_flow


def main():
    capacity, start, finish, n = build_graph_from_matrix('in.txt')
    source = start - 1
    target = finish - 1
    flow_matrix, max_flow = ford_fulkerson(capacity, source, target)
    output_flow = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            output_flow[i][j] = max(0, flow_matrix[i][j])

    with open('out.txt', 'w') as f:
        for i in range(n):
            f.write(' '.join(str(output_flow[i][j]) for j in range(n)))
            f.write('\n')
        f.write(str(max_flow))


if __name__ == "__main__":
    main()
