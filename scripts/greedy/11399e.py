import sys

n = int(input())
p = list(map(int, sys.stdin.readline().split()))
total = 0

psorted_ = sorted(p)

for i in range(1, n+1):
    total += sum(psorted_[0:i])

print(total)

# 1 2 3 3 4

# 1 2+1 3+3 3+6 4+9
# 1 3   6   9   13