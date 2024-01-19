import sys
sys.setrecursionlimit(300000)

n, m = map(int, input().split())
yangachi = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global v, k
    visited[y][x] = 1
    if yangachi[y][x] == 'v':
        v += 1
    elif yangachi[y][x] == 'k':
        k += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and yangachi[ny][nx] != '#' and visited[ny][nx] == 0:
            dfs(nx, ny)

wolf, sheep = 0, 0

for i in range(n):
    for j in range(m):
        if yangachi[i][j] != '#' and visited[i][j] == 0:
            v, k = 0, 0
            dfs(j, i)
            if v >= k:
                k = 0
            else:
                v = 0

            wolf += v
            sheep += k

print(sheep, wolf)