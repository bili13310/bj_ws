star = int(input())

for i in range(2*star):
    if i <= (star-1):
        print(" "*(star-1-i)+"*"*(2*(1+i)-1))
    elif i > (star-1):
        print(" "*(i-(star-1))+"*"*(2*(2*star-1-i)-1))