n = int(input())
students= []
ans = []

for _ in range(n):
    weight, height = map(int, input().split())
    students.append((weight, height))

for i in range(n):
    cnt = 0
    for j in range(n):
        if students[i][0] < students[j][0] and students[i][1] < students[j][1]:
            cnt += 1
    ans.append(cnt+1)

for k in ans:
    print(k, end=' ')