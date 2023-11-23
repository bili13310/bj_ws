N = int(input())
B = 0

for l in range(N):
    S = list(str(input()))
    A = [S[0]]

    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            A.append(S[i+1])

    if len(A) == len(set(A)):
        pass
    else:
        B += 1



print(N - B)