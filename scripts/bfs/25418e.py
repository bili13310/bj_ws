from collections import deque
import sys
input = sys.stdin.readline

a, k = map(int, input().split())
cnt = 0
d = [1, 2]
views = [0] * (k+2)

def bfs(x, cnt):
    deq.append((x, cnt))
    views[x] = 1

    while deq:
        x, cnt = deq.popleft()
        if x == k:
            return cnt

        for i in [x+d[0], x*d[1]]:
            if i <= k and views[i] == 0:
                views[i] = 1
                deq.append((i, cnt+1))

deq = deque()
cnt = bfs(a, cnt)
print(cnt)