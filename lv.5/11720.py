import sys

N = int(input())
M = str(input())
tot = 0

for i in range(N):
    tot += int(M[i])

print(tot)