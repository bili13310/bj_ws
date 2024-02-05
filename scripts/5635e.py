n = int(input())

bd =[]
for _ in range(n):
    n, d, m, y = map(str, input().split())
    d, m, y = map(int, (d, m, y))
    bd.append((y, m, d, n))
bd.sort()
print(bd[-1][3])
print(bd[0][3])


