import sys

A = []
B = 0

for i in range(10):
    A.append(int(input()) % 42)

A = set(A)
print(len(A))
# 중복되는 것들은 하나로 통일
# 결과로 남은 것의 개수만 세면 돼