import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
v = int(input())
sum = 0

for i in range(N):
    if v == A[i]:
        sum += 1
    else:
        pass

print(sum)
