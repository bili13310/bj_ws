# 13m

A = int(input())
B = int(input())

C = B // 100
D = (B % 100) // 10
E = B % 10

if 100 <= A <= 999 and 100 <= B <= 999:
    print(A * E)
    print(A * D)
    print(A * C)
    print(A * B)
else:
    ValueError