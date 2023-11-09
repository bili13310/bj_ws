import sys

N,M = map(int, sys.stdin.readline().split())

bucket = [0 for z in range(N)]

for x in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for y in range(i, j+1):
        bucket[y-1] = k

print(*bucket)