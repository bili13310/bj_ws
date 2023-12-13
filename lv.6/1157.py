import sys

S = list(str(input()))

A = list(0 for i in range(26))

for i in range(65, 91):
    for j in range(len(S)):
        if chr(i).lower() == S[j].lower():
            A[i-65] += 1
        else:
            pass

MAX = max(A)

if A.count(MAX) >= 2:
    print("?")
else:
    print(chr(A.index(MAX)+65))