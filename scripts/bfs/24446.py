from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
field = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    field[u].append(v)
    field[v].append(u)

def bfs(x):
    deq.append(x)
    visited[x] = 0

    while deq:
        x = deq.popleft()
        field[x].sort()
        for k in field[x]:
            if visited[k] == -1:
                visited[k] = visited[x] + 1
                deq.append(k)


deq = deque()
bfs(r)
for i in visited[1:]:
    print(i)