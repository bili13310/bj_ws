import sys

def dfs(rows, cols):
    if matrix[rows][cols] == '-':
        matrix[rows][cols] = 1
        for a in [1, -1]:
            Y = cols + a
            if 0 <= Y < M and matrix[rows][Y] == '-':
                dfs(rows, Y)

    if matrix[rows][cols] == '|':
        matrix[rows][cols] = 1
        for b in [1, -1]:
            X = rows + b
            if 0 <= X < N and matrix[X][cols] == '|':
                dfs(X, cols)

N, M = map(int, sys.stdin.readline().split())
matrix = []
cnt = 0

for _ in range(N):
    matrix.append(list(input()))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == '-' or matrix[i][j] == "|":
            dfs(i, j)
            cnt += 1

print(cnt)