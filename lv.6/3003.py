import sys

K, Q, R, B, k, P = map(int, sys.stdin.readline().split())

if K > 1:
    K = -(K-1)
else:
    K = abs(K-1)
if Q > 1:
    Q = -(Q-1)
else:
    Q = abs(Q-1)
if R > 2:
    R = -(R-2)
else:
    R = abs(R-2)
if B > 2:
    B = -(B-2)
else:
    B = abs(B-2)
if k > 2:
    k = -(k-2)
else:
    k = abs(k-2)
if P > 8:
    P = -(P-8)
else:
    P = abs(P-8)

print(K,Q,R,B,k,P)