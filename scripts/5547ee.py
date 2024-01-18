import sys
input = sys.stdin.readline()

w, h = map(int, input.split())
buildings = [list(map(int, input.split())) for _ in range(h)]
visited = [[0] * w for _ in range(h)]
cnt = 0
dx = [1, 1, 1, -1, -1, -1]
dy = [0, 1, -1, 0, 1, -1]

def dfs(x, y):
    if y % 2 == 0:


    elif y % 2 != 0:
    # global cnt
    # cnt += 1

    # for k in range(6):
    #     nx, ny = x + dx[k], y + dy[k]
    #     if buildings[ny][nx] 



for i in range(h):
    for j in range(w):
        if buildings[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)

print(cnt)