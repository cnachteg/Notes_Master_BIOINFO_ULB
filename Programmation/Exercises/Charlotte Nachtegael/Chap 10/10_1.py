def ackermann(m,n):
    if m == 0:
        res = n+1
    elif m > 0 and n == 0:
        res = ackermann(m-1,1)
    else:
        y = ackermann(m,n-1)
        res = ackermann(m-1,y)
    return res

print(ackermann(3,6))