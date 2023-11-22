import sys

S = str(input())

for i in range(97, 123):
    A = S.find(chr(i))
    if A >= 0:
        print(A, end=" ")
    else:
        print(-1, end=" ")