import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = 0
tot = 0

for i in range(N):
    if M < A[i]:
        M = A[i]
    else:
        pass

for j in range(N):
    A[j] = A[j]/M * 100
    tot += A[j]

print(tot/N)