import sys

h,w = map(int, sys.stdin.readline().split())
city = []
answer = [[0] * w for _ in range(h)]
cloud = 0

for _ in range(h):
    city.append(list(map(str, input())))

for i in range(h):
    for j in range(w):
        if cloud == 0 and city[i][j] == '.':
            answer[i][j] = -1
        elif city[i][j] == 'c':
            cloud = 1
            answer[i][j] = 0
            num = 1
        elif cloud == 1 and city[i][j] == '.':
            answer[i][j] = num
            num += 1
    cloud = False
    num = 1

for x in range(h):
    for y in range(w):
        print(answer[x][y], end=' ')
    print()

# c가 있거나,   곧 나오거나,         아예 오지 않거나
#   0       c의 위치에 따라 값 출력     초깃값을 -1로 설정하기
# c를 만났으면 족속성 발생
            
# -1 -1 -1 0 1 2 3 4