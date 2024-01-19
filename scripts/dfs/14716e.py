import sys
sys.setrecursionlimit(3000000)

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def dfs(y, x):
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= ny < n and 0 <= nx < m:
            if word[ny][nx] == 1:
                word[ny][nx] = 0
                dfs(ny, nx)

n, m = map(int, input().split())
word = []
for _ in range(n):
    word.append(list(map(int, input().split())))

tot = 0
for i in range(n):
    for j in range(m):
        if word[i][j] == 1:
            word[i][j] = 0
            dfs(i, j)
            tot += 1
print(tot)