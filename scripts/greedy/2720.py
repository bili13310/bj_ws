import sys

Testcase = int(input())
change = []

for i in range(Testcase):
    change.append(int(input()))

have = [25, 10, 5, 1]
button = [0 for i in range(len(have))]

for j in range(Testcase):
    for k in have:
        button[have.index(k)] = change[j] // k
        change[j] %= k
    print("{0} {1} {2} {3}".format(button[0], button[1], button[2], button[3]))