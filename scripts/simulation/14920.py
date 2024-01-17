import sys

c = int(input())
cnt = 0

while c > 1:
    if c % 2 == 0:
        cnt += 1
        c = c / 2
    elif c % 2 != 0:
        cnt += 1
        c = 3*c + 1

print(cnt+1)