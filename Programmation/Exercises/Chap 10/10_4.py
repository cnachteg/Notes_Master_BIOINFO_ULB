def puissance(x,n):
    if n == 1:
        res = x
    if n ==0:
        res = 1
    else:
        res = x*puissance(x,n-1)
    return res

print(puissance(4,3))
