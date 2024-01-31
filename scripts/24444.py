from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
field = [[] for _ in range(n+1)]
views = [0] * (n+1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    field[u].append(v)
    field[v].append(u)

def bfs(x):
    global count
    deq.append(x)
    views[x] = 1

    while deq:
        x = deq.popleft()
        field[x].sort()
        for k in field[x]:
            if views[k] == 0:
                count += 1
                views[k] = count
                deq.append(k)

deq = deque()
bfs(r)
for i in views[1:]:
    print(i)