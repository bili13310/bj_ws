import sys
input = sys.stdin.readline

n = int(input())
line = 1

while line < n:
    n -= line
    line += 1

if line % 2 == 0:
    up = n
    down = line - n + 1

else:
    up = line - n + 1
    down = n

print("{0}/{1}".format(up, down))


# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2/ 4/1
