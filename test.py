import sys

N, M, L = map(int, sys.stdin.readline().split())
A = [0]*N
cnt = i = 0

while A[i] < M-1:
    A[i] += 1
    cnt += 1
    i = (i+L) % N if A[i] % 2 == 1 else (i-L) % N

print(cnt)