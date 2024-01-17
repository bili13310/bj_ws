import sys

A = []
time = 0

for _ in range(5):
    A.append(int(input()))
    
while A[0] < A[1]:
    if A[0] < 0:
        time += A[2]
        A[0] += 1
    elif A[0] == 0:
        time += A[3] + A[4]
        A[0] += 1
    elif A[0] > 0:
        time += A[4]
        A[0] += 1

print(time)

# -10
# 20
# 5
# 10
# 3

# 50
# 10
# 60
# 120
