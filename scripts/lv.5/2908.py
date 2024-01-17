import sys

A, B = map(str, sys.stdin.readline().split())

# AA = list(A[2-i] for i in range(3))
# BB = list(B[2-j] for j in range(3))

# A = "{0}{1}{2}".format(AA[0], AA[1], AA[2])
# B = "{0}{1}{2}".format(BB[0], BB[1], BB[2])

# if int(A) > int(B):
#     print(A)
# elif int(A) < int(B):
#     print(B)

A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)