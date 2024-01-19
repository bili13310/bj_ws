폭이

# import sys

# input = sys.stdin.readline
# n = int(input())

# # ↗ ( 1, 1)  > ↑ ( 2, 0) / ↘ (-1, 1) : 0 > 5,1
# # ↘ (-1, 1)  > ↗ ( 1, 1) / ↓ (-2, 0) : 1 > 0,2
# # ↓ (-2, 0)  > ↙ (-1,-1) / ↘ (-1, 1) : 2 > 3,1
# # ↙ (-1,-1)  > ↖ ( 1,-1) / ↓ (-2, 0) : 3 > 4,2
# # ↖ ( 1,-1)  > ↙ (-1,-1) / ↑ ( 2, 0) : 4 > 3,5
# # ↑ ( 2, 0)  > ↖ ( 1,-1) / ↗ ( 1, 1) : 5 > 4,0
# # (x + 1) % 6 = a
# # (x + 5) % 6 = b
# mx = [1, -1, -2, -1, 1, 2]
# my = [1, 1, 0, -1, -1, 0]

# # 최댓값 : 22 * 2 * 2 = 100


# def dfs(x, y, idx, cnt):
#   nx = x + mx[idx]
#   ny = y + my[idx]

#   if visited[nx][ny]:
#     if cnt == n:
#       return 1
#     else:
#       return 0
#   if cnt == n:
#     return 0
#   visited[nx][ny] = True
#   result = 0
#   xIdx = (idx + 1) % 6
#   yIdx = (idx + 5) % 6
#   result += dfs(nx, ny, xIdx, cnt + 1)
#   result += dfs(nx, ny, yIdx, cnt + 1)
#   visited[nx][ny] = False

#   return result


# visited = [[False] * 101 for _ in range(101)]
# visited[50][50] = True
# print(dfs(50, 50, 0, 0))