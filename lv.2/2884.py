# 8min

H, M = map(int, input().split())

if 0 <= H <= 23 and 0 <= M <= 59:
    if M >= 45:
        print(H, M-45)
    elif M < 45:
        FH = H -1
        FM = 60 + M - 45
        if FH < 0:
            print(23, FM)
        else:
            print(FH, FM)

else:
    ValueError