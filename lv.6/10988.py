import sys

S = list(str(input()))
H = list(reversed(S))

if S == H:
    print(1)
else:
    print(0)