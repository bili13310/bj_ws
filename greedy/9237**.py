import sys

N = int(input())
t = list(map(int, sys.stdin.readline().split()))

t = sorted(t, reverse=True)

for i in range(N):
    t[i] = i + t[i] + 1

print(max(t) + 1)


# 인덱스로 접근하는게 시간이 더 오래걸리나봐..!
# import sys
# N = int(input())
# t = list(map(int, sys.stdin.readline().split()))
# t = sorted(t, reverse=True)
# for i in t:
#     t[t.index(i)] = i + t.index(i) + 1
# print(max(t) + 1)



# 2 3 4 3
# 3 5 7  7

# 4 3 3 2
# 5 5 6 6 7

# 39 38 9  35 39 20
# 40 40 12 39 44 26

# 39 39 38 35 20 9
# 40 41 41 39 25 15