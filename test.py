import sys

h, w = map(int, sys.stdin.readline().split())
cloud = False
city = []
answer = [[0] * w for _ in range(h)]

for i in range(h):
    city.append(list(input()))

for x in range(h):
    for y in range(w):
        if cloud == False and city[x][y] == '.':
            answer[x][y] = -1
        elif city[x][y] == 'c':
            cloud = True
            num = 1
            answer[x][y] = 0
        elif cloud == True and city[x][y] == '.':
            answer[x][y] = num
            num += 1
    cloud = False
    num = 1

# for a in range(h):
#     for b in range(w):
#         print(answer[a][b], end=' ')
#     print()