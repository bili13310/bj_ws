dial = ['ABC', "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

num = list(input())
tot = 0

for i in dial:
    for j in num:
        if j in str(i):
            tot += (dial.index(i) + 3)

print(tot)

# S = str(input())
# tot = 0

# for i in range(len(S)):
#     if 65 <= ord(S[i]) < 68:
#         tot += 3
#     elif 68 <= ord(S[i]) < 71:
#         tot += 4
#     elif 71 <= ord(S[i]) < 74:
#         tot += 5
#     elif 74 <= ord(S[i]) < 77:
#         tot += 6
#     elif 77 <= ord(S[i]) < 80:
#         tot += 7
#     elif 80 <= ord(S[i]) < 84:
#         tot += 8
#     elif 84 <= ord(S[i]) < 86:
#         tot += 9
#     elif 86 <= ord(S[i]) < 90:
#         tot += 10
#     elif int(S[i]) == 1:
#         tot += 2
#     elif int(S[i]) == 0:
#         tot += 11

# print(tot)


# print(ord(S))

# A-C 65-67
# D-F 68-70
# G-I 71-73
# J-L 74-76
# M-O 77-79
# P-S 80-83
# T-V 84-86
# W-Z 87-90