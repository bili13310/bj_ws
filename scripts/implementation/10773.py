from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
deq = deque()

for _ in range(k):
    a = int(input())
    if a == 0:
        deq.pop()
    else:
        deq.append(a)
    
print(sum(deq))