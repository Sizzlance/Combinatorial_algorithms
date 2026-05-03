from collections import deque
import sys


def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        while ptr < len(data) and data[ptr] == '0':
            ptr += 1
        friends = []
        while ptr < len(data) and data[ptr] != '0':
            f = int(data[ptr])
            friends.append(f)
            ptr += 1
        ptr += 1

        for f in friends:
            adj[i].append(f)
            adj[f].append(i)

    for i in range(1, N + 1):
        if not adj[i]:
            print(0)
            return

    color = [None] * (N + 1)

    for i in range(1, N + 1):
        if color[i] is None:
            queue = deque([i])
            color[i] = 0
            while queue:
                v = queue.popleft()
                for u in adj[v]:
                    if color[u] is None:
                        color[u] = 1 - color[v]
                        queue.append(u)

    valid = True
    for v in range(1, N + 1):
        has_friend_in_other_team = False
        for u in adj[v]:
            if color[u] != color[v]:
                has_friend_in_other_team = True
                break
        if not has_friend_in_other_team:
            valid = False
            break

    if not valid:
        color = [0] * (N + 1)
        valid = True
        for v in range(1, N + 1):
            has_friend_in_other_team = False
            for u in adj[v]:
                if color[u] != color[v]:
                    has_friend_in_other_team = True
                    break
            if not has_friend_in_other_team:
                valid = False
                break

        if not valid:
            print(0)
            return

    team0 = [i for i in range(1, N + 1) if color[i] == 0]
    team1 = [i for i in range(1, N + 1) if color[i] == 1]

    if len(team0) <= len(team1):
        print(len(team0))
        if team0:
            print(' '.join(map(str, team0)))
    else:
        print(len(team1))
        if team1:
            print(' '.join(map(str, team1)))


if __name__ == "__main__":
    main()
