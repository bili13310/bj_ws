# 원래: 1 2 3 4 5
# 1st: 2 1 3 4 5
# 2nd: 2 1 4 3 5
# 3rd: 3 4 1 2 5
# 4th: 3 4 1 2 5

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
K = list(j+1 for j in range(N))
N = list(i+1 for i in range(N))

for x in range(M):
    a, b = map(int, sys.stdin.readline().split())
    for y in range(b-a+1):
        K[a-1+y] = N[b-1-y]
    N.clear()
    N.append(K)
    N = list(itertools.chain(*N))

print(*K)