import sys 

paid = int(input())
rest = 1000 - paid
change = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in change:
    cnt += rest // i
    rest %= i

print(cnt)

# import sys

# paid = int(input())
# change = 1000 - paid
# cnt = 0

# while True:
#     if change >= 500:
#         cnt += change // 500
#         change = change % 500
#     elif change >= 100:
#         cnt += change // 100
#         change = change % 100
#     elif change >= 50:
#         cnt += change // 50
#         change = change % 50
#     elif change >= 10:
#         cnt += change // 10
#         change = change % 10
#     elif change >= 5:
#         cnt += change // 5
#         change = change % 5
#     else:
#         cnt += change // 1
#         break

# print(cnt)