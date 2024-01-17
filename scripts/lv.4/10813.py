import sys

N, M = map(int, sys.stdin.readline().split())

bucket = [i+1 for i in range(N)]
spare = [0]

for x in range(M):
    i, j = map(int, sys.stdin.readline().split())
    spare[0] = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = spare[0]

    # bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]

print(*bucket)