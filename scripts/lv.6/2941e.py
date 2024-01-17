croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = str(input())

for i in croatia:
    S = S.replace(i, "*")

print(len(S))

# S = str(input())
# A = len(S)

# for i in range(len(S)):
#     if S[i] == "c":
#         if S[i+1] == "=" or S[i+1] == "-":
#             A -= 1

#     elif S[i] == "d":
#         if S[i+1] == "z" and S[i+2] == "=ㄴ":
#             A -= 1
#         elif S[i+1] == "-":
#             A -= 1
#         else:
#             pass

#     elif S[i] == "n" or S[i] == "l":
#         if S[i+1] == "j":
#             A -= 1
#         else:
#             pass
    
#     elif S[i] == "s" or S[i] == "z":
#         if S[i+1] == "=":
#             A -= 1
#         else:
#             pass

# print(A)