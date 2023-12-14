import sys

N = int(input())
P = list(map(int, sys.stdin.readline().split()))
total = 0

P = sorted(P)

for i in range(N):
    total += sum(P[0:i+1])

print(total)