import sys

A=list(map(int, input()))
B=list(map(int, input()))
arr = [0] * 16

for i in range(16):
    if i % 2 == 0:
        arr[i] = A[i//2]
    elif i % 2 != 0:
        arr[i] = B[i//2]

while len(arr) != 2:
    temp = []
    for j in range(len(arr)-1):
        temp.append((arr[j]+arr[j+1]) % 10)
    arr = temp

print(*arr, sep="")