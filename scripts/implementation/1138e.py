import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
temp = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == num[i] and temp[j] == 0:
            temp[j] = i+1
            break
        elif temp[j] == 0:
            cnt += 1
print(*temp)