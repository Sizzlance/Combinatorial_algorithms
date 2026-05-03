def read_input(filename):
    with open(filename, 'r') as file:
        n, k = map(int, file.readline().split())
        bridges = []

        for _ in range(k):
            a, b, date = file.readline().split()
            bridges.append((int(a), int(b), date))

    return n, bridges


def dfs(v, graph, visited):
    visited[v] = True
    for to in graph[v]:
        if not visited[to]:
            dfs(to, graph, visited)


def is_connected(graph, n):
    visited = [False] * (n + 1)
    dfs(1, graph, visited)

    for i in range(1, n + 1):
        if not visited[i]:
            return False

    return True


def find_unification_day(n, bridges):
    graph = [[] for _ in range(n + 1)]

    for a, b, date in bridges:
        graph[a].append(b)
        graph[b].append(a)

        if is_connected(graph, n):
            return date

    return None


def main():
    n, bridges = read_input('in.txt')
    answer = find_unification_day(n, bridges)

    with open('out.txt', 'w') as file:
        if answer is not None:
            file.write(answer)


if __name__ == "__main__":
    main()
