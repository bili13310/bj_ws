import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

print("{0} {1}".format(min(A), max(A)))