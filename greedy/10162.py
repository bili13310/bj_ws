import sys

time = int(input())
cook = [300, 60, 10]
need = list(0 for i in range(len(cook)))


for i in range(len(cook)):
    need[i] += time // cook[i]
    time %= cook[i]

if time != 0:
    print(-1)
else:
    print("{0} {1} {2}".format(need[0], need[1], need[2]))