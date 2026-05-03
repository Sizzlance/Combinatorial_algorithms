from collections import deque

n = int(input())
graph = {}
distance = {}

for _ in range(n):
    team = input().split()
    for player in team:
        if player not in graph:
            graph[player] = set()

    for i in range(3):
        for j in range(i + 1, 3):
            graph[team[i]].add(team[j])
            graph[team[j]].add(team[i])

if 'Isenbaev' in graph:
    queue = deque()
    queue.append('Isenbaev')
    distance['Isenbaev'] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

for player in sorted(graph.keys()):
    if player in distance:
        print(player, distance[player])
    else:
        print(player, "undefined")
