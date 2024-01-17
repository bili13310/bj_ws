import sys

turn = list(str(input()))
inside = [1, 0, -1]
num = 0

for _ in range(len(turn)):
    if turn[_] == 'A':
        num = inside[1]
        inside[1] = inside[0]
        inside[0] = num

    elif turn[_] == 'B':
        num = inside[2]
        inside[2] = inside[1]
        inside[1] = num
    elif turn[_] == 'C':
        num = inside[2]
        inside[2] = inside[0]
        inside[0] = num 

print(inside.index(1)+1)

# li = [1, 0, 0]
# s = input()
# for c in s:
#     if c == 'A':
#         li[0], li[1] = li[1], li[0]
#     elif c == 'B':
#         li[1], li[2] = li[2], li[1]
#     else:
#         li[0], li[2] = li[2], li[0]
# print(li.index(1) + 1)