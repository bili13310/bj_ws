point = []
temp = []
tot = 0

for i in range(8):
    point.append(int(input()))

for j in range(5):
    tot += max(point)
    temp.append(point.index(max(point))+1)
    point[point.index(max(point))] = -1
temp.sort()

print(tot)
print(*temp)
