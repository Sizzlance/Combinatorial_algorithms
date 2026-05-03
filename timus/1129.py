from collections import deque

maxn = 100

color = [[False] * (maxn + 1) for _ in range(maxn + 1)]
mult = [[0] * (maxn + 1) for _ in range(maxn + 1)]


class Node:
    def __init__(self, node_id):
        self.visited = False
        self.out = []
        self.id = node_id


v = [Node(i) for i in range(maxn + 1)]


def addmult(a, b, x):
    mult[a][b] += x
    mult[b][a] += x


def addedge(a, b):
    a.out.append(b)
    b.out.append(a)


def explore(u):
    u.visited = True
    q = deque()
    current = u

    while current.out:
        w = current.out.pop()
        if mult[current.id][w.id] > 0:
            addmult(current.id, w.id, -1)
            if mult[current.id][w.id] == 0:
                color[current.id][w.id] = True
            current = w
            q.append(current)

    while q:
        explore(q.popleft())


def even(n):
    odd = []
    for i in range(1, n + 1):
        if len(v[i].out) % 2 != 0:
            odd.append(v[i])

    for i in range(0, len(odd), 2):
        addedge(odd[i], odd[i + 1])
        addmult(odd[i].id, odd[i + 1].id, 1)


def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0

    n = int(input[ptr])
    ptr += 1

    input_data = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        v[i].id = i

    for i in range(1, n + 1):
        m = int(input[ptr])
        ptr += 1
        input_data[i] = []
        for _ in range(m):
            u = int(input[ptr])
            ptr += 1
            input_data[i].append(u)
            if i < u:
                addmult(v[i].id, u, 1)
                addedge(v[i], v[u])

    even(n)

    for i in range(1, n + 1):
        if not v[i].visited:
            explore(v[i])

    for i in range(1, n + 1):
        output = []
        for u in input_data[i]:
            output.append('Y' if color[i][u] else 'G')
        print(' '.join(output))


if __name__ == "__main__":
    main()