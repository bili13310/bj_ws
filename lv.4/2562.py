A = []

for i in range(9):
    A.append(int(input()))
    max_value = A[0]
    max_num = 1

for j in range(9):
    if max_value < A[j]:
        max_value = A[j]
        max_num = j+1
    else:
        max_value = max_value
        max_num = max_num

print(max_value)
print(max_num)
