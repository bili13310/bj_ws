import sys
C = []
cnt = 0

N = int(input())
for i in range(N):
    C.append(int(input()))

C.sort(reverse=True)

for i in range(len(C)):
    if (i+1) % 3 != 0:
        cnt += C[i]

print(cnt)