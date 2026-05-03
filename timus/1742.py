import sys
from collections import deque


def solve():
    n = int(sys.stdin.readline())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(sys.stdin.readline())

    visited = [False] * (n + 1)
    min_groups = 0

    for i in range(1, n + 1):
        if not visited[i]:
            path = []
            current = i
            while True:
                if visited[current]:
                    if current in path:
                        idx = path.index(current)
                        cycle = path[idx:]
                        min_groups += 1
                    break
                visited[current] = True
                path.append(current)
                current = a[current]

    visited = [False] * (n + 1)
    max_groups = 0

    for i in range(1, n + 1):
        if not visited[i]:
            max_groups += 1
            current = i
            while True:
                if visited[current]:
                    break
                visited[current] = True
                next_node = a[current]
                if next_node == current:
                    break
                current = next_node

    print(min_groups, max_groups)


solve()