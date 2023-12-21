import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
buckets = [i for i in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    buckets = buckets[:i] + buckets[k:j+1] + buckets[i:k] + buckets[j+1:]
    
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