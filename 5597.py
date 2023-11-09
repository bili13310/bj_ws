N = []
M = [i+1 for i in range(5)]

for i in range(3):
    N.append(int(input()))

for j in M:
    for k in range(3):
        if N[k] == M[j]:
            M.remove(k)
            print(M)