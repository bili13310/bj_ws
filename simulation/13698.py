buckets = [1, 0, 0, 2]
alpha = list(input())

for i in alpha:
    if i == 'A':
        buckets[0], buckets[1] = buckets[1], buckets[0]
    elif i == 'B':
        buckets[0], buckets[2] = buckets[2], buckets[0]
    elif i == 'C':
        buckets[0], buckets[3] = buckets[3], buckets[0]
    elif i == 'D':
        buckets[1], buckets[2] = buckets[2], buckets[1]
    elif i == 'E':
        buckets[1], buckets[3] = buckets[3], buckets[1]
    elif i == 'F':
        buckets[2], buckets[3] = buckets[3], buckets[2]

print(buckets.index(1)+1)
print(buckets.index(2)+1)