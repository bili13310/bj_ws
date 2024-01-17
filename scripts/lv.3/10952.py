import sys

A = 1
B = 1

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    print(A+B)