from collections import deque

r, c = map(int, input().split())
ultari = [list(input()) for _ in range(r)]
views = [[0] * c for _ in range(r)]
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
wolves = 0
sheep = 0

def bfs(y, x):
    deq.append((y, x))
    o = 0
    v = 0

    while deq:
        y, x = deq.popleft()
        for k in range(5):
            nx, ny = x+dx[k], y+dy[k]

            if 0 <= ny < r and 0 <= nx < c and views[ny][nx] == 0:
                if ultari[ny][nx] == '#':
                    continue
                elif ultari[ny][nx] == 'v':
                    v += 1
                elif ultari[ny][nx] == 'o':
                    o += 1
                deq.append((ny, nx))
                views[ny][nx] = 1
    return o, v
        
deq = deque()
for i in range(r):
    for j in range(c):
        if ultari[i][j] != '#' and views[i][j] == 0:
            s, w = bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolves += w
print(sheep, wolves)

