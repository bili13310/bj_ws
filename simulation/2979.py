import sys

A, B, C = map(int, sys.stdin.readline().split())

check = [0 for _ in range(100)]
result = 0

for j in range(3):
    x, y = map(int, sys.stdin.readline().split())
    for k in range(x,y):
        check[k-1] += 1

result += C * (check.count(3)) * 3
result += B * check.count(2) * 2
result += A * check.count(1)

print(result)

# 1 2 3 4 5 6 7 8
# [         ]   
#     [   ]
#   [           ]

# 3 2 * 3 * 1 = 6
# 2 2 * 2 * 3 = 12
# 1 3 * 1 * 5 = 15

# 33