import sys

N, M = map(int, sys.stdin.readline().split())
buckets = [x+1 for x in range(N)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    buckets = buckets[:i-1] + buckets[k-1:j] + buckets[i-1:k-1] + buckets[j:]
    
print(*buckets)


# 1 2 3 4 5 6 7 8 9 10

# 1 6 4
# 4 5 6 1 2 3 7 8 9 10

# 3 9 8
# 4 5 8 9 6 1 2 3 7 10

# 2 10 5
# 4 6 1 2 3 7 10 5 8 9

# 1 3 3
# 1 4 6 2 3 7 10 5 8 9

# 2 6 2
# 1 4 6 2 3 7 10 5 8 9