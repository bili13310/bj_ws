from collections import deque
import sys
input = sys.stdin.readline

field = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r,c = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

def bfs(y, x):
    global cnt
    deq.append((y, x, 0))
    visited[y][x] = 1

    while deq:
        y, x, cnt = deq.popleft()
        if field[y][x] == 1:
            return cnt
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
                if field[ny][nx] == -1:
                    continue
                else:
                    visited[ny][nx] = 1
                    deq.append((ny, nx, cnt+1))

deq = deque()
cnt = bfs(r, c)
print(-1 if cnt == None else cnt)

# from collections import deque
# import sys
# input = sys.stdin.readline

# field = [list(map(int, input().split())) for _ in range(5)]
# visited = [[0] * 5 for _ in range(5)]
# r,c = map(int, input().split())
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# cnt = 0

# def bfs(y, x):
#     global cnt
#     deq.append((y, x))
#     visited[y][x] = 1

#     while deq:
#         y, x = deq.popleft()
#         if field[y][x] == 1:
#             return cnt
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
#                 if field[ny][nx] == -1:
#                     continue
#                 else:
#                     visited[ny][nx] = 1
#                     cnt += 1
#                     deq.append((ny, nx))

# deq = deque()
# cnt = bfs(r, c)
# print(-1 if cnt == None else cnt)