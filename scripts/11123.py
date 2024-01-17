import sys
sys.setrecursionlimit(30000)

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())

    chowon = [list(input()) for _ in range(h)]
    views = [[0] * w for _ in range(h)]
    cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(x, y):
        views[y][x] = 1

        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            if 0 <= nx < w and 0 <= ny < h and chowon[ny][nx] == '#' and views[ny][nx] == 0:
                dfs(nx, ny)

    for i in range(h):
        for j in range(w):
            if chowon[i][j] == '#' and views[i][j] == 0:
                cnt += 1
                dfs(j, i)

    print(cnt)