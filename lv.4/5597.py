import sys

N = []
M = [i+1 for i in range(30)]
F = [j+1 for j in range(30)]

for i in range(28):
    N.append(int(sys.stdin.readline()))

for j in range(len(N)):
    for k in F:
        if N[j] == M[k-1]:
            F.remove(k)

for i in F:
    print(i)