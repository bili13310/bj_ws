n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

field.sort()

for i in range(n):
    print(field[i][0], field[i][1])