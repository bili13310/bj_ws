import sys

T = int(input())

for i in range(T):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)
    for i in range(len(S)):
        for j in range(R):
            print(S[i], end="")
    print()