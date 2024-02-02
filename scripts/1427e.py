sort = list(map(int, input()))

sort.sort(reverse=True)
for i in range(len(sort)):
    print(sort[i], end='')