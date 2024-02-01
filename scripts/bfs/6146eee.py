from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999)

x, y, n = map(int, input().split())
field = [['.'] * 1000 for _ in range(1000)]
visited = [[0] * 1000 for _ in range(1000)]
dw = [1, -1, 0, 0]
dz = [0, 0, 1, -1]
cnt = 0
field[x+500][y+500] = 'B'

for _ in range(n):
    a, b = map(int, input().split())
    field[a+500][b+500] = 'M'

def bfs(w, z):
    deq.append((w, z, 0))
    visited[w+500][z+500] = 1

    while deq:
        w, z, cnt = deq.popleft()
        if field[w+500][z+500] == 'B':
            return cnt
        
        for i in range(4):
            nw, nz = w+dw[i], z+dz[i]
            if 0 <= nw < 1000 and 0 <= nz < 1000 and visited[nw+500][nz+500] == 0:
                if field[nw+500][nz+500] == 'M':
                    continue
                else:
                    visited[nw+500][nz+500] = 1
                    deq.append((nw, nz, cnt+1))

deq = deque()
cnt = bfs(0, 0)
print(cnt)