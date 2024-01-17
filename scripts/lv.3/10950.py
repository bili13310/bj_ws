# 5min

T = int(input())
A = []
B = []

for i in range(T):
    C, D = map(int, input().split())
    A.append(C)
    B.append(D)
    
for j in range(T):
    print(A[j] + B[j])

# 출력의 때를 따로 신경써줄 필요없어
# T = int(input())

# for i in range(T):
#     A, B = map(int, input().split())
#     print(A + B)