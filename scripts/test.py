import sys
sys.setrecursionlimit(300000)

from collections import deque

r, c = map(int, input().split())
ultari = [list(input()) for _ in range(r)]
views = [[0] * c for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    views[y][x] = 1
    global v, k
    
    if ultari[y][x] == 'v' or ultari[y][x] == 'k':
        deq.append(ultari[y][x])

    for a in range(4):
        nx, ny = x + dx[a], y + dy[a]
        if 0 <= nx < c and 0 <= ny < r and ultari[ny][nx] != '#' and views[ny][nx] == 0:
            dfs(nx, ny)


deq = deque()
wolf, sheep = 0, 0
for i in range(r):
    for j in range(c):
        if ultari[i][j] != '#' and views[i][j] == 0:
            deq.clear()
            dfs(j, i)
            k = deq.count('k')
            v = deq.count('v')
            if v >= k:
                k = 0
            elif v < k:
                v = 0
            wolf += v
            sheep += k

print(sheep, wolf)