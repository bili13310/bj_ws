n = int(input())

field = [list(map(int, input().split())) for _ in range(n)]

for j in range(n):
    field[j][0] , field[j][1] = field[j][1], field[j][0]

field.sort()

for i in range(n):
    print(field[i][1], field[i][0])

# n = int(input())

# field = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n-1):
#     for j in range(i+1, n):
#         if field[i][1] > field[j][1]:
#             field[i], field[j] = field[j], field[i]
#         elif field[i][1] == field[j][1]:
#             if field[i][0] > field[j][0]:
#                 field[i], field[j] = field[j], field[i]

# for i in range(5):
#     print(field[i][0], field[i][1])