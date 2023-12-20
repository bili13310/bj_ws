import sys

N, L = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))

while True:
    if L >= min(h):
        L += 1
        h.pop(h.index(min(h)))
        if h == []:
            break
    elif L < min(h):
        break

print(L)