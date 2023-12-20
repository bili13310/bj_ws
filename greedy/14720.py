# import sys

# N = int(input())
# milk = list(map(int, sys.stdin.readline().split()))
# me = 0
# cnt = 0

# for i in range(len(milk)):
#     if milk[i] == me:
#         me = me + 1
#         cnt += 1
#         if me > 2:
#             me = 0
#     elif milk[i] != me:
#         pass

# print(cnt)

import sys

n = int(input())
milk = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(n):
    if milk[i] == cnt % 3:
        cnt += 1
print(cnt)