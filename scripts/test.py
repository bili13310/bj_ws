from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
field = [[0] * n for _ in range(n)]
d = [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]


def bfs(y, x):
    deq.append((y, x))
    field[y][x] = 0

    while deq:
        y, x = deq.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and field[ny][nx] == 0:
                deq.append((ny, nx))
                field[ny][nx] = field[y][x] + 1

deq = deque()
bfs(r1, c1)
print(-1 if field[r2][c2] == 0 else field[r2][c2])