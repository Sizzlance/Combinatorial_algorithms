n = int(input())
lectures = []
max_time = 30000

for _ in range(n):
    s, e = map(int, input().split())
    lectures.append((s, e))

count = [0] * (max_time + 2)
for s, e in lectures:
    count[e] += 1

prefix = [0] * (max_time + 2)
for e in range(1, max_time + 1):
    prefix[e] = prefix[e - 1] + count[e - 1]

sorted_lectures = [None] * n
for s, e in lectures:
    sorted_lectures[prefix[e]] = (s, e)
    prefix[e] += 1

result = 0
last_end = -1
for s, e in sorted_lectures:
    if s > last_end:
        result += 1
        last_end = e

print(result)
