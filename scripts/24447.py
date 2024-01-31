from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
field = [[] for _ in range(n+1)]
views = [-1, 0] * (n+1)
print(views)

count = 1
for _ in range(m):
    u, v = map(int, input().split())
    field[u].append(v)
    field[v].append(u)

def bfs(x):
    global count
    deq.append(x)
    views[x][0] = 0

    while deq:
        x = deq.popleft()
        field[x].sort()

        for k in field[x]:
            if views[k][0] == -1:
                count += 1
                views[k] = [views[x][0]+1, count]
                deq.append(k)
deq = deque()
bfs(r)
ans = 0

for v in views:
    ans += v[0] * v[1]
print(ans)

# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m, r = map(int, input().split())
# fieldd = [[] for _ in range(n+1)]
# fieldt = [[] for _ in range(n+1)]
# viewsd = [-1] * (n+1)
# viewst = [0] * (n+1)
# count = 1
# sum = 0

# for _ in range(m):
#     u, v = map(int, input().split())
#     fieldd[u].append(v)
#     fieldd[v].append(u)
#     fieldt[u].append(v)
#     fieldt[v].append(u)

# def bfsd(y):
#     deqd.append(y)
#     viewsd[y] = 0

#     while deqd:
#         y = deqd.popleft()

#         for t in fieldd[y]:
#             if viewsd[t] == -1:
#                 viewsd[t] = viewsd[y] + 1
#                 deqd.append(t)


# def bfst(x):
#     global count
#     deqt.append(x)
#     viewst[x] = 1

#     while deqt:
#         x = deqt.popleft()
#         fieldt[x].sort()

#         for d in fieldt[x]:
#             if viewst[d] == 0:
#                 count += 1
#                 viewst[d] = count
#                 deqt.append(d)

# deqd = deque()
# deqt = deque()
# bfsd(r)
# bfst(r)

# for i in range(len(viewsd)-1):
#     sum += viewsd[i+1] * viewst[i+1]

# print(sum)