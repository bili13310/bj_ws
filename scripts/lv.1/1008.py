# 15분

A, B = map(int, input().split())

if 0 < A and B < 10:
    C = A / B
    if abs(C - A/B) <= 10**-9:
        print(A /B)
else:
    ValueError