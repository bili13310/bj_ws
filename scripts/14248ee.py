# import sys
# from collections import deque

# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# n = int(input())
# stone = list(map(int, input().split()))
# s = int(input())
# visited = [False] * (n+1)
# cnt = 0

# def dfs(x):
#     global cnt
#     if x < 0 or n <= x:
#         return

#     if not visited[x]:
#         visited[x] = True
#         cnt +=1
#         dfs(x - stone[x])
#         dfs(x + stone[x])

# dfs(s-1)
# print(cnt)

import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
stone = list(map(int, input().split()))
s = int(input())
visited = [False] * n
cnt = 1

deq = deque()
deq.append(s-1) # s-1 = 2 => deq에 2를 넣어
visited[s-1] = 1

while deq:
    x = deq.popleft()
    for a in [stone[x], -stone[x]]:
        X = x + a
        if 0 <= X < n and visited[X] == 0:
            visited[X] = 1
            cnt += 1
            deq.append(X)
print(cnt)