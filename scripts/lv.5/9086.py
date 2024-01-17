import sys

N = int(input())

for i in range(N):
    S = str(input())
    print("{0}{1}".format(S[0],S[len(S)-1]))