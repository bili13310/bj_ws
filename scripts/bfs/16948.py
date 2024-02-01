from collections import deque
import sys
input = sys.stdin.readline
deq = deque()

def bfs(y, x):
    deq.append((y, x))
    field[y][x] = 0

    while deq:
        y, x = deq.popleft()
        for dy, dx in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and field[ny][nx] == 0:
                deq.append((ny, nx))
                field[ny][nx] = field[y][x] + 1


N = int(input())
field = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
d = [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]
bfs(r1, c1)
print(-1 if field[r2][c2] == 0 else field[r2][c2])

# [ ][ ][o][ ][ ]
# [o][ ][ ][ ][o]
# [ ][ ][o][ ][ ]
# [o][ ][ ][ ][o]
# [ ][ ][o][ ][ ]
#                [ ]
#                   [ ]