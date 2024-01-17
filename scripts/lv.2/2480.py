# 20min

A, B, C = map(int, input().split())

if 1 <= A <= 6 and 1 <= C <= 6 and 1 <= B <= 6:
    if A == B == C:
        price = 10000 + A * 1000
        print(price)
    
    elif A == B != C or B == C != A or A == C != B:
        if abs(A - B) == 0:
            price = 1000 + A * 100
            print(price)
        elif abs(B - C) == 0:
            price = 1000 + C * 100
            print(price)
        elif abs(C - A) == 0:
            price = 1000 + C * 100
            print(price)
    elif A != B != C:
        if A > B > C or A > C > B:
            price = A * 100
            print(price) 
        elif B > C > A or B > A > C:
            price = B * 100
            print(price)
        elif C > A > B or C > B > A:
            price = C * 100
            print(price)
else:
    ValueError