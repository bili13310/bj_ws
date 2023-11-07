# 28min

A, B = map(int, input().split())
C = int(input())

if 0 <= A <= 23 and 0 <= B <= 59 and 0 <= C <= 1000:
    FM = B + C
    FH = A
    if FM >= 60:
        D =  FM // 60
        FH = A + D
        FM = FM % 60
        if FH >= 24:
            FH = FH - 24
            print(FH, FM)
        elif 0 <= FH <= 23:
            print(FH, FM)
    else:
        print(FH, FM)
else:
    ValueError