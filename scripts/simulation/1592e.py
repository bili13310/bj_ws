import sys

N, M, L = map(int, sys.stdin.readline().split())
cnt = i = 0
A = [0 for _ in range(N)]

while A[i] < M-1:
    A[i] += 1
    cnt += 1
    i = (i+L)%N if A[i] % 2 == 1 else (i-L)%N

print(cnt)

# 1 -> 4
# 4 -> 2
# 2 -> 5
# 5 -> 3
# 3 -> 1
# 1 -> 3
# 3 -> 5
# 5 -> 2
# 2 -> 4
# 4 -> 1

# 1 5 4 3 2
# 2 2 2 2 2